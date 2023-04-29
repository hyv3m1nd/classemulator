#!/bin/env python
import sys, inspect

from pyats import aetest
from pyats.aetest.loop import Iteration
from pyats.easypy import run
from ats.log.utils import banner

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
from steps import Steps
Steps.set_log(log)

from sste_common_emulator import SsteCommonEmulator
sste_common = SsteCommonEmulator()

import sste_exr, sste_cxr, sste_trigger, sste_cli_keys, sste_spitfire, sste_tgn
from class_emulator import ClassEmulator
sste_tgn = ClassEmulator(sste_tgn)
sste_trigger = ClassEmulator(sste_trigger)
sste_exr = ClassEmulator(sste_exr)
sste_cxr = ClassEmulator(sste_cxr)
sste_cli_keys = ClassEmulator(sste_cli_keys)
sste_spitfire = ClassEmulator(sste_spitfire)

import yaml, pdb, json
from texttable import Texttable
import re, random, time, collections
from functools import reduce
from time import time, sleep
from typing import Any, Union
from cgi import test

def tree(): return collections.defaultdict(tree)

class Globals: pass


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def build_test_environment(self, testscript, testbed, steps, test_data):
        testscript.parameters['script_args'] = tree()
        script_args = testscript.parameters['script_args']

        script_args['testsuitename'] = __file__
        if 'connect_via' in test_data:
            script_args['sste_connect_via'] = test_data['connect_via']

        if 'testsuite' in test_data:
            script_args['testsuitename'] = test_data['testsuite']
        
        if 'testgroup' in test_data:
            script_args['testsuitename'] = test_data['testgroup']
        
        script_args['check_bgp_convergence'] = 0
        if ('bgp_convergence' in test_data) and (test_data['bgp_convergence'] == 1) :
            script_args['check_bgp_convergence'] = 1

        script_args['check_convergence_time'] = 0
        if ('tgn' in test_data) and ('tgn_convergence_check' in test_data) and (test_data['tgn_convergence_check'] == 1) :
                script_args['check_convergence_time'] = 1
        
        script_args['ping_test_result'] = {}

        testscript.parameters['timing'] = tree()
        timing = testscript.parameters['timing']

        Globals.testscript = testscript
        Globals.timing = timing
        Globals.script_args = script_args
        Globals.testbed = testbed
        Globals.steps = steps
        Globals.test_data = test_data
        Globals.info = test_data

        for sste_emulator in [sste_common, sste_tgn, sste_trigger, sste_exr, sste_cxr, sste_cli_keys, sste_spitfire]:
            sste_emulator.save_reference_object(Globals)
        
        Steps.set_steps(steps)

    @aetest.subsection
    def establish_connections(self):
        if 'UUT' in Globals.test_data:
            def connect_to_uut():
                Globals.script_args['uut'] = sste_common._get_connection(devicename=Globals.test_data['UUT'])
                sste_common.get_version_info()
            Steps.start("Connecting to UUT") \
                (connect_to_uut)()

        if 'tgn' in Globals.test_data:
            def connect_to_tgn():
                if not sste_tgn.tgn_connect(device=Globals.test_data['tgn']):
                    Steps.failed("Cannot connect to TGN")
            Steps.start("Connecting to TGN") \
                (connect_to_tgn)()
            

class xr_ping_test(aetest.Testcase):
    @aetest.test
    def ping(self):
        if "ping_test_ip_list" in Globals.test_data and str(Globals.test_data["ping_test_ip_list"]).strip() != "":
            def ping_ip_list():
                ips = Globals.test_data['ping_test_ip_list'].split(",")
                for ip in ips:
                    if ip.strip() != "":
                        Globals.script_args['ping_test_result'][ip] = sste_trigger.ping(ip=ip)
                        if not Globals.script_args['ping_test_result'][ip]:
                            if 'debug_ping_clis' in Globals.test_data:
                                cmds = Globals.test_data['debug_ping_clis'].split(",")
                            else:
                                cmds = ["show log last 200", "show bgp neighbor brief", "show interface all | file harddisk:/show_interface_all.log", "show isis neighbor"]
                            sste_common.exec_commands(cmds)
            Steps.start("Pinging") \
                (ping_ip_list)()
            

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self):
        def disconnect_all_devices():
            if Globals.testbed.devices:
                for host, connection in Globals.testbed.devices.items():
                    if connection:
                        log.info(f"Disconnecting from {host}")
                        connection.disconnect()
        Steps.start("Disconnect Devices") \
            (disconnect_all_devices)()

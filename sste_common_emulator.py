"""
Emulates a library of functions called sste_common, replacing sste_common.exec_commands().

By default, exec_commands accepts two arguments: 
    args, and
    script_args.

args is a dictionary that contains the command(s) we wish to run. It takes the form of {
    "sste_commands": <a ist of string commands>
}
alternatively, args can be a string representation of the dictionary, such as: '{"sste_commands": ["cmd_1", "cmd_2", ..., "cmd_N"]}'

script_args contains meta-data that we do not touch.

We will make exec_commands accept one parameter:
    commands.

commands can be either a command string or a list of commands.
For backward compatibility purposes, it can also be a dictionary or the string form of the dictionary.

script_args can also be passed into exec_commands() through **kwargs. Alternatively, it can be stored as a class attribute.

@author Ben Hsieh
"""
from class_emulator import ClassEmulator
import sste_common
from typing import Union, List
import ast


class SsteCommonEmulator(ClassEmulator):
    def __init__(self, **kwargs):
        super().__init__(sste_common, **kwargs)


    def exec_commands(self, commands: Union[list, str, dict], **kwargs):
        """
        Prerequisites: 
        1. script_args must be saved as a parameter.
        1. script_args['uut'] must be set using script_args['uut'] = sste_common._get_connection(devicename=...)
        """
        try:
            commands = ast.literal_eval(commands)
        except ValueError:
            pass

        if isinstance(commands, str):
            commands = [commands]
        if isinstance(commands, list):
            commands = {
                "sste_commands": commands
            }
        return super().__getattr__("exec_commands")(commands, **kwargs)
    
    
    def __getattr__(self, function_name):
        """
        Current hypothesis: This needs to be redefined below any function definition, or it would overwrite the functions above
        # TODO work out how exactly this works with any overwritten function
        """
        return super().__getattr__(function_name)

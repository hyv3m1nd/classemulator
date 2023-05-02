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

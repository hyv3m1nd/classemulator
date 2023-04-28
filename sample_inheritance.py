from class_emulator import ClassEmulator
import emulated_library
from typing import Union, List


class EmulatorForSpecificLibrary(ClassEmulator):
    def __init__(self, **kwargs):
        super().__init__(emulated_library, **kwargs)


    def exec_commands(self, commands: Union[list, str, dict], **kwargs):
        """
        The emulated library has an exec_commands function, which takes the following arguments:
        args: a dictionary that must have "commands", which must be a list of strings,
        other arguments that are stored in the emulator
        """
        if isinstance(commands, str):
            commands = [commands]
        if isinstance(commands, list):
            commands = {
                "commands": commands
            }
        return super().__getattr__("exec_commands")(commands, **kwargs)
    
    
    def __getattr__(self, function_name):
        """
        Current hypothesis: This needs to be redefined below any function definition, or it would overwrite the functions defined
        # TODO work out how exactly this works with any overwritten function
        """
        return super().__getattr__(function_name)

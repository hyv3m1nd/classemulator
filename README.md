# Class Emulator
This project seeks to cause object-like behavior in non-OOP libraries or enhance polymorphism in objects by hiding any repetitive function parameter.  
It can emulate classes or objects.  

## Example
""" We will attempt to emulate json.dumps() with indent, without passing indent into json.dumps()'s parameters."""  
from emulator import ClassEmulator  
import json  

json_emulator = ClassEmulator(json, indent=4)  

data_to_print = {"speaker": "Jonathan", "message": "Hello!"}  

emulated_dumps_output = json_emulator.dumps(data_to_print)  

print(emulated_dumps_output)  

## Example Output
{  
&emsp;&emsp;&emsp;&emsp;"speaker": "Jonathan",  
&emsp;&emsp;&emsp;&emsp;"message": "Hello!"  
}  

## Explanation
The main class is **emulator/ClassEmulator**. It has 4 functions:  
    **\_\_init\_\_(self, target_class, \*\*kwargs)**: emulates the target class with any number of named function parameters.  
    **save_params(self, \*\*kwargs)**: adds named function parameters.  
    **save_reference_object(self, reference_object, copy_attributes: bool)**: saves an object from which we can reference its attributes, or copies its attributes to our attributes list.  
    **\_\_getattr\_\_(self, name)(*args, \*\*kwargs)**: the centerpiece of the emulator, it allows you to call any function in the emulated class with any named and unnamed parameter, while automatically filling in any appropriate named parameters you stored.  

## Other files
**example.py**: a functional example with explanations in the output.  
**simple_printer.py**: a short script that allows example.py to showcase that an imported module may be emulated directly.  
**sste_common_emulator.py**: a real-life inheritance example. Note that sste_common.py is proprietary and not provided here.  
**experimental_emulator.py**: an early version of emulator.py, which contains documentations of other libraries and code that may be useful.  
**steps.py**: a work in progress and a part of a broader plan to reimagine how my team uses the pyats testing framework. This is not directly related to classemulator. It is instead used to simplify a pattern of putting try-except in a step, which is used extensively in my team.  
**emulator_test.py**: a simplified version of a real-life pyats test. It combines classemulator, steps, and a singleton-facade I call Globals together to refactor my team's testing framework. Note that this test requires a yaml file, which is converted into test_data, as well as a testbed file. These files contain proprietary information and are not provided.  

## Requirements
This class is written in Python 3.9.13 or above. Backward compatibility with earlier versions may be possible but is not guaranteed.  
No outside library is required.  

## Back Story
I have been working with a team that develops and uses its own library for router testing. The library has been vetted for handling complex use cases throughout the years.  
  
However, it could use better OOP structuring and software design. Of note, (1) functions repetitively call the same parameters that the end user does not edit, distracting programmers. (2) Due to the increasing number of device connection solutions such as Paramiko, Netmiko, and Napalm and the unique features they offer to handle different connection types and CLI outputs, as well as the increase in official vendor-supplied API's such as Open Ixia, a bridge design will be helpful for future development. This calls for a switch to OOP-based design. Furthermore, (3) some features such as automatic responses to CLI prompts currently reside in the overall test framework library but should be encapsulated in connection objects instead.  
   
Unfortunately, it is impractical to redesign it, since it is also massive (8000+ lines per file), tightly coupled with the data it manages, and the foundation of over a decade's worth of proprietary code.  
  
I designed classemulator as the start of a software design improvement. Its purpose is to move toward OOP by coupling object attributes with the appropriate objects in a framework not designed with OOP in mind.  
  
Started developing in April 2023


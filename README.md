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
    **\_\_getattr\_\_(self, name)(*args, \*\*kwargs)**: allows you to call any function in the emulated class with any named and unnamed parameter.  

## Other files
example.py: a functional example with explanations in the output.  
simple_printer.py: a short script that allows example.py to showcase that an imported module may be emulated directly.  
sste_common_emulator.py: a real-life inheritance example. Note that sste_common.py is proprietary and not provided here.  
experimental_emulator.py: an early version of emulator.py, which contains documentations of other libraries and code that may be useful.  
steps.py: a work in progress and a part of a broader plan to reimagine how my team uses the pyats testing framework. This is not directly related to classemulator.  
emulator_test.py: a pyats test that combines classemulator, steps, and a singleton-facade together to refactor my team's testing framework.  

## Requirements
This class is written in Python 3.9.13 or above. Backward compatibility with earlier versions may be possible but is not guaranteed.  
No outside library is required.  

## Back Story
I have been working with a team that develops and uses its own library for router testing. The library has been vetted for handling complex use cases throughout the years. However, it could use better OOP structuring. Of note, functions repetitively call the same parameters that the end user does not edit, distracting programmers.  
Unfortunately, it is impractical to redesign it, since it is also massive (8000+ lines per file) and tightly coupled with the data it manages.  
I designed classemulator to hide redundant arguments that belong in OOP and help me focus on the function arguments that matter.  
  
Started developing in April 2023


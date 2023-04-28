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
The main class is emulator/ClassEmulator. It has 4 functions:  
    **\_\_init\_\_(self, target_class, \*\*kwargs)**: emulates the target class with any number of named function parameters.  
    **save_params(self, \*\*kwargs)**: adds named function parameters.  
    **save_reference_object(self, reference_object, copy_attributes: bool)**: saves an object from which we can reference its attributes, or copies its attributes to our attributes list.  
    **\_\_getattr\_\_(self, name)(*args, \*\*kwargs)**: allows you to call any function in the emulated class with any named and unnamed parameter.  

## Requirements
This class is written in Python 3.9.13 or above. Backward compatibility with earlier versions may be possible but is not guaranteed.  
No outside library is required.  

## Back Story
I have been working with a team that develops and uses its own library for router testing. The library has been vetted for handling complex use cases throughout the years. It is also massive (8000+ lines per file) and tightly coupled with the data it manages. This makes it impractical to re-design the entire library.  
However, it could use better OOP structuring. Of note, functions repetitively call the same parameters that the end user does not edit, distracting programmers.   
I designed classemulator to hide redundant arguments that belong in OOP and help me focus on the function arguments that matter.  


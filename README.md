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
The main class is emulator/ClassEmulator. It has 3 functions:  
    __init__(self, target_class, **kwargs): emulates the target class with any number of named function parameters.  
    save_params(self, **kwargs): adds named function parameters.  
    __getattr__(self, name)(*args, **kwargs): allows you to call any function in the emulated class with any named and unnamed parameter.  

## Requirements
This class is written in Python 3.9.13 or above. Backward compatibility with earlier versions may be possible but is not guaranteed.  
No outside library is required.  

## Back Story
A year ago, I joined a team that has been developing and using its own library for router testing for years.  
The library is extensive (8000+ lines per file), covers several scenarios, and bug-free.  
That is to say, the library is vetted through years of use to handle complex tasks well. It is also massive and tightly coupled with the data it manages. This makes it impractical to re-design the entire library.  
However, it is poorly designed and documented. Of note, functions repetitively call the same parameters that the end user does not edit. This makes it very distracting to use.   
I designed classemulator to hide redundant arguments that belong in OOP and help me focus on the function arguments that matter.  


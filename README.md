# Class Emulator
This simple class is used to reduce the redundancy of any poorly written code with repetitive function parameters.  
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
The library is extensive (8000+ lines per file) and covers several scenarios.  
However, it is poorly documented and designed from an OOP perspective. All function parameters are named "args", "script_args", "module_args", etc. Each arg is a dictionary with no documentation; and many parameters are not meant to be changed by end users but are nonetheless repeatedly passed into functions.  
That is to say, the library is powerful but difficult and very distracting to use. The team wishes to continue using it.  
I designed classemulator to help me focus on the function arguments that matter and stop passing the same redundant arguments into every function.  


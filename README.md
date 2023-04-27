# classemulator
This simple class is used to reduce the redundancy of any poorly written code with repetitive function parameters.
It can emulate classes or objects.

Requirement:
This class is written in Python 3.9.13 or above. Backward compatibility with earlier versions may be possible but is not guaranteed.
No outside library is required. 

Back Story:
A year ago, I joined a team that has been developing and using its own library for router testing for years. 
The library is extensive (8000+ lines per file) and covers several scenarios. 
However, it is poorly documented and designed from an OOP perspective. All function parameters are named "args", "script_args", etc; they are all dictionaries with no documentation; and many parameters are not meant to be changed by end users but are nonetheless repeatedly passed into functions.
That is to say, the library is powerful but difficult to use. The team wishes to continue using it.
I designed classemulator to reduce the need to repetitively pass in the same arguments into every function.


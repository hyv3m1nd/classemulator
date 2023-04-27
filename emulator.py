"""
This class is used to cause object-like behavior in non-OOP libraries or enhance polymorphism in objects.  
It does so by saving any repetitive parameter in its attributes and passing it into any function that can accept them.  
For a demo, see example.py
@author Ben Hsieh
"""
import inspect


class ClassEmulator:
    def __init__(self, target_class, **kwargs):
        """
        Creates a target_class emulator and stores any function parameter as self attributes.

        Parameters
        ----------
        target_class: class or object
            The target to emulate. Can be anything with its own library of functions.
        **kwargs: any key=value
            Any additional parameters to store and use in target_class's functions.
        """
        self.__target_class = target_class
        self.save_params(**kwargs)

    def save_params(self, **kwargs):
        """
        Stores any parameter you may want to pass into functions as class attributes.

        Parameters
        ----------
        **kwargs: any key=value
            Any parameter to store and use in target_class's functions.
        """
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __getattr__(self, function_name):
        """
        Runs the named function with any stored applicable parameter and any parameter the user passes in.
        """

        def run_named_function(*args, **kwargs):
            target_function = getattr(self.__target_class, function_name)

            target_function_parameters = [
                parameter
                for i, parameter in enumerate(target_function.__code__.co_varnames)
                if i > 0 or parameter != "obj"
            ]

            stored_parameters = {
                key: value
                for key, value in self.__dict__.items()
                if key != "_ClassEmulator__target_class"
            }

            parameters = {
                key: value
                for key, value in stored_parameters.items()
                if "kwargs" in target_function_parameters
                or key in target_function_parameters
            }

            parameters.update(kwargs)

            return target_function(*args, **parameters)

        return run_named_function

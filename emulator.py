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
        self.__reference_objects = []
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

    def save_reference_object(self, reference_object, copy_attributes: bool=False) -> None:
        """
        Saves an object from which we can look up attributes.
        Newer references' attributes will overwrite older references' attributes.
        Self attributes will overwrite any reference object attributes.
        If copy_attributes, the reference object's attributes are copied to self attributes, and the reference object is then discarded.
        """
        if copy_attributes:
            reference_object_attributes = reference_object.__dict__
            self.save_params(**reference_object_attributes)
        
        else:
            self.__reference_objects.append(reference_object)
            
    def __getattr__(self, function_name):
        """
        Runs the named function with any stored applicable parameter and any parameter the user passes in.
        """

        def run_named_function(*args, **kwargs):
            target_function = getattr(self.__target_class, function_name)

            target_function_parameters = [
                parameter
                for i, parameter in enumerate(target_function.__code__.co_varnames)
                if i > 0 or parameter != "obj" #TODO check if there are other cases where a non-parameter would be referenced 
            ]

            stored_parameters = {}
            for reference_object in self.__reference_objects:
                for key, value in reference_object.__dict__.items():
                    stored_parameters[key] = value
            for key, value in self.__dict__.items():
                if key != "_ClassEmulator__target_class": #TODO make this more generic for inheritance, or discard altogether
                    stored_parameters[key] = value

            parameters = {
                key: value
                for key, value in stored_parameters.items()
                if "kwargs" in target_function_parameters
                or key in target_function_parameters
            }

            parameters.update(kwargs)

            return target_function(*args, **parameters)

        return run_named_function

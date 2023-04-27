"""
This documents the experimental code and related tests.
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
            Any additional parameters to store and use in target_class's functions
        """
        print(type(target_class))
        self.target_class = target_class
        self.set_default_params(**kwargs)

    def set_default_params(self, **kwargs):
        """
        Stores any parameter you may want to pass into functions as class attributes.

        Parameters
        ----------
        **kwargs: any key=value
            Any parameter to store and use in target_class's functions
        """
        for key, value in kwargs.items():
            print(f"self.{key} = {value}")
            self.__setattr__(key, value)

    def __getattr__(self, name):
        # fakes any function from another class or object and prints out its accepted parameters beforehand
        def run_named_function(*args, **kwargs):
            target_function = getattr(self.target_class, name)

            target_function_parameters = [
                parameter
                for i, parameter in enumerate(target_function.__code__.co_varnames)
                if i > 0 or parameter != "obj"
            ]

            stored_parameters = {
                key: value
                for key, value in self.__dict__.items()
                if key != "target_class"
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


class json_dumps_emulator:
    """
    This class is unused. It documents some python code that may come in handy for my ClassEmulator class.
    For my purpose, it will emulate json and have one function: dumps()
    """

    def dumps(*args, **kwargs):
        import json

        function_name = inspect.stack()[0][3]  # get current function name
        json_function = getattr(
            json, function_name
        )  # get corresponding function in json library
        print(json_function(*args, **kwargs))


class test_target_class:
    """
    A class with a static function and a class function
    """

    def __init__(self):
        self.one = 1

    def print_one(self):
        print(self.one)

    def static_func(*args, **kwargs):
        pass


if __name__ == "__main__":
    import json

    json_emulator = ClassEmulator(json, indent=4)

    data = {"a": "bcd", "e": "fgh"}
    str_repr = json_emulator.dumps(data)
    print(str_repr)

    test_target_class_emulator = ClassEmulator(test_target_class)
    test_target_class_emulator.static_func()

    test_target_object_emulator = ClassEmulator(test_target_class())
    test_target_object_emulator.print_one()

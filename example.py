from emulator import ClassEmulator
import simple_printer
import json


data_to_print = {"speaker": "Jonathan", "message": "Hello!"}

print("We start with this data:")
print(data_to_print)
print("")


class ClassMethodTester:
    @classmethod
    def retrieve(cls, data, key):
        return data[key]


class_method_tester_emulator = ClassEmulator(ClassMethodTester)
data_retrieved = class_method_tester_emulator.retrieve(data_to_print, "speaker")
print(
    "ClassEmulator can handle @classmethod and run the @classmethod retrieve('speaker') function:"
)
print(f"emulator.retrieve(data, 'speaker') -> {data_retrieved}")
print("")

print_emulator = ClassEmulator(simple_printer)
print(
    "We can emulate a file with no classes and use its print(data) function to get the results:"
)
print_emulator.print_data(data_to_print)
print("")

dumps_output_without_indent = json.dumps(data_to_print)
print(
    "Next, we will emulate the json library. By default, json.dumps(data) returns the following:"
)
print(dumps_output_without_indent)
print("")

dumps_output_with_indent = json.dumps(data_to_print, indent=4)
print("json.dumps(data, indent=4) returns the following:")
print(dumps_output_with_indent)
print("")

json_emulator_with_indent = ClassEmulator(json, indent=4)
emulated_dumps_output = json_emulator_with_indent.dumps(data_to_print)
print(
    "Using an emulator that stores indent=4, we can get dumps(data) to return the following without passing indent=4 into dumps() directly:"
)
print(emulated_dumps_output)
print("")

json_emulator_with_indent.set_default_params(
    garbage_parameter="I will break your code!"
)
emulated_dumps_output = json_emulator_with_indent.dumps(data_to_print)
print(
    "Also, any attribute that json.dumps() cannot accept is disregarded. For example, passing garbage_parameter yields the following:"
)
print(emulated_dumps_output)
print("")

print(
    "Note that this does not prevent json.dumps() from throwing an error if you pass an unacceptable parameter directly into emulator.dumps():"
)
json_emulator_with_indent.dumps(
    data_to_print, garbage_parameter="I will break your code!"
)

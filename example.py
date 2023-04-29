from emulator import ClassEmulator
import simple_printer
import json


data_to_print = {"speaker": "Jonathan", "message": "Hello!"}

print_emulator = ClassEmulator(simple_printer)
print("We can emulate a python file that is imported directly and use its simple_print(data) function to get the results:")
print_emulator.print_data(data_to_print)


dumps_output_without_indent = json.dumps(data_to_print)
print("By default, json.dumps(data) returns the following:")
print(dumps_output_without_indent)
print("")

dumps_output_with_indent = json.dumps(data_to_print, indent=4)
print("json.dumps(data, indent=4) returns the following:")
print(dumps_output_with_indent)
print("")

json_emulator_with_indent = ClassEmulator(json, indent=4)
emulated_dumps_output = json_emulator_with_indent.dumps(data_to_print)
print(
    "Using an emulator that stores indent=4, we can get emulator.dumps(data) to return the following without passing indent=4 into dumps() directly:"
)
print(emulated_dumps_output)
print("")

json_emulator_with_indent.save_params(
    garbage_parameter="I will break your code!"
)
emulated_dumps_output = json_emulator_with_indent.dumps(data_to_print)
print(
    "Also, any attribute that json.dumps() cannot accept is disregarded. For example, if emulator has stored garbage_parameter, emulator.dumps(data) yields the following:"
)
print(emulated_dumps_output)
print("")

print(
    "Note that this does not prevent json.dumps(data) from throwing an error if you pass an unacceptable parameter directly into emulator.dumps():"
)
json_emulator_with_indent.dumps(
    data_to_print, garbage_parameter="I will break your code!"
)

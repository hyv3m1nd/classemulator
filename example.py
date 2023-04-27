from emulator import ClassEmulator
import json


data_to_print = {"speaker": "Jonathan", "message": "Hello!"}

dumps_output_without_indent = json.dumps(data_to_print)
print("By default, json.dumps() returns the following:")
print(dumps_output_without_indent)
print("")

dumps_output_with_indent = json.dumps(data_to_print, indent=4)
print("json.dumps(data, indent=4) returns the following:")
print(dumps_output_with_indent)
print("")

json_emulator_with_indent = ClassEmulator(json, indent=4)
emulated_dumps_output = json_emulator_with_indent.dumps(data_to_print)
print(
    "Using an emulator that stores indent=4, we can get dumps() to return the following without passing indent=4 into dumps() directly:"
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

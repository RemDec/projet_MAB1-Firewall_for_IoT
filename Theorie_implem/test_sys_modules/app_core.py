import importlib

i = importlib.import_module("mod_test")
mod_test = i.get_module()

print(mod_test.get_description())
mod_test.start()

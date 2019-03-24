import importlib

nmap = importlib.import_module("mod_test").get_module()
blank = importlib.import_module("mod_blank").get_module()
blank.set_params({"prog":"ping", "args":"192.168.0.1"})

nmap.start()
blank.start()

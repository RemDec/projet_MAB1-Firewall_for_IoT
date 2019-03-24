from time_queue import *
import importlib

nmap = importlib.import_module("mod_test").get_module()
blank = importlib.import_module("mod_blank").get_module()
#blank.set_params({"prog":"ping", "args":"192.168.0.1 -c 1"})

blank.set_init_timer(20)

q = Time_queue(blank, nmap)
decr = Decr_timer(1, q)

print(q)
decr.start_decr()

#nmap.start()
#blank.start()

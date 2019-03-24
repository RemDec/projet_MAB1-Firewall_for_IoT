from module import *

class Active_module(Module):

    def set_init_timer(self, t):
        self.init_timer = t
        
    def is_active(self):
        return True

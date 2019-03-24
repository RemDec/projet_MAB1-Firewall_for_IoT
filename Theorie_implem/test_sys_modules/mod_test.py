from module_act import *
import subprocess

def get_module():
    return AModule_test()
    
    
class AModule_test(Active_module):
    
    def __init__(self, params = None):
        self.m_id = "test"
        
        self.CMD = "nmap"
        self.PARAMS = {"port":("80", True, "-p"), "IP":("192.168.0.0/24", True,""), 
                       "options":("-sV", False, "")}
          
        self.set_init_timer(60)
        self.set_params(params)
        
    def set_params(self, params):
        self.params = self.treat_params({} if params is None else params)
    
    def distrib_output(self):
        pass
        
    def treat_params(self, params):
        final_par = {}
        for par, val in self.PARAMS.items():
            if params.get(par):
                final_par[par] = params[par]
            elif val[1]:
                final_par[par] = val[0]
        return final_par
        
    def start(self):
        cmd = [self.CMD]
        for param, val in self.params.items():
            cmd.append(self.PARAMS[param][2] + val)
        print(cmd)
        end_proc = subprocess.run(cmd)
        
    def stop(self):
        pass
    
    def get_description(self):
        return "Module de test (actif) lançant un scan nmap basique"

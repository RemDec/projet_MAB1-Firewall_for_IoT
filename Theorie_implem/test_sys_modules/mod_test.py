from module_act import *


def get_module(params=None, timer=30):
    return AModule_test(params, timer)


class AModule_test(Active_module):

    def __init__(self, params = None, timer=60):
        self.m_id = "test"

        self.CMD = "nmap"
        self.PARAMS = {"port":("80", True, "-p"), "IP":("192.168.0.0/24", True,""),
                       "options":("-sV", False, "")}
        # ou nom_param :  (val_defaut, obligatoire, prefixe)
        self.set_init_timer(timer)
        self.set_params(params)

    def set_params(self, params):
        self.params = super().treat_params(self.PARAMS, {} if params is None else params)

    def distrib_output(self, script_output):
        print(f"Module [{self.m_id}] execution returned :\n{script_output.stdout}")

    def start(self):
        cmd = [self.CMD]
        for param, val in self.params.items():
            cmd.append(self.PARAMS[param][2] + val)
        s_thread = self.get_script_thread()
        s_thread.start(cmd)

    def get_script_thread(self):
        return Script_thread(callback_fct=self.distrib_output)

    def stop(self):
        pass

    def get_description(self):
        return f"[{self.m_id}]Module de test (actif) lançant un scan nmap basique"

    def get_module_id(self):
        return self.m_id

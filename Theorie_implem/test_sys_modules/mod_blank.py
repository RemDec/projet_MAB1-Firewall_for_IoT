from module_act import *

def get_module(params=None, timer=5):
    return AModule_blank(params, timer)

class AModule_blank(Active_module):

    def __init__(self, given_params=None, timer=60):
        self.m_id = "blank"
        self.PARAMS = {"prog":("echo", True, ""),
                       "args":("No or bad command given to blank module", False, "")}
        self.set_params(given_params)
        self.set_init_timer(timer)

    def get_description(self):
        return f"[{self.m_id}]Module blanc exécutant toute commande complète donnée en argument"

    def get_module_id(self):
        return self.m_id

    def set_params(self, params):
        self.params = super().treat_params(self.PARAMS, {} if params is None else params)

    def start(self):
        s_thread = self.get_script_thread()
        if self.params.get("args") is None:
            self.params["args"] = self.PARAMS["args"][0] if self.params["prog"] == "echo" else ""
        s_thread.start([ self.params["prog"]] + self.params["args"].split())

    def get_script_thread(self):
        return Script_thread(callback_fct=self.distrib_output)

    def stop(self):
        pass

    def distrib_output(self, script_output):
        cmd = script_output.args
        print(f"Arbitrary command {cmd} executed with output : \n{script_output.stdout}")

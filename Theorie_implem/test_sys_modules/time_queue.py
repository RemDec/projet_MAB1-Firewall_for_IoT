from threading import Timer


class Time_queue():

    def __init__(self, *modules):
        self.q = [] + list(modules)
        self.resort()

    def add(self, module):
        ind = 0
        for q_mod in self.q:
            if q_mod.timer > module.timer:
                ind +=1
        self.q.insert(ind, module)

    def resort(self):
        self.q = sorted(self.q, key= lambda mod: mod.timer, reverse=True)

    def decr_queue(self, call_exp=True):
        for mod in self.q:
            if call_exp:
                mod.decr_timer(call_exp=mod.start)
        self.resort()
        print(self)

    def __str__(self):
        m = ""
        for mod in self.q:
            i =  "+---------------------------\n"
            i += "| [" + str(mod.get_module_id()) + "]\n"
            i += "| timer :" + str(mod.timer) + "\n"
            i += "+---------------------------\n"
            m += i + "              Î\n              |\n"
        return m




class Decr_timer():
    def __init__(self, interval, queue):
        self._timer     = None
        self.interval   = interval
        self.is_running = False
        self.queue = queue

    def _run(self):
        self.is_running = False
        self.queue.decr_queue()
        self.start_decr()

    def start_decr(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

from passive_job import *
import threading
import pipes
import time


class Module_thread(threading.Thread):

    def __init__(self, pipe_name):
        threading.Thread.__init__(self)
        self.pipe_name = pipe_name

    def run(self):
        self.pass_job = Passive_job(pipe_name, self.cmd)
        self.pass_job.launch()

    def start(self, cmd):
        self.cmd = cmd
        super().start()


pipe_name = 'pip'
pipe = pipes.Template()

th = Module_thread(pipe_name)
th.start(['ping', '192.168.0.1'])
cnt = 1
output = None
pos = 0
while cnt<6:
    try:
        if output is None:
            output = pipe.open(pipe_name, 'r')
            print("---", cnt, " ouverture read pipe ---")
            pos = output.tell()
        else:
            pos = output.seek(pos)
            print("---------------", cnt, "pos:",pos, "----------------\n" + output.read())
            pos = output.tell()
    except FileNotFoundError as e:
        print("tube non existant, attente 3s")
    time.sleep(3)
    cnt += 1

output.seek(0, 0)
print("avant close:\n" + output.read())
th.pass_job.stop()
print("apres close:\n" + output.read())

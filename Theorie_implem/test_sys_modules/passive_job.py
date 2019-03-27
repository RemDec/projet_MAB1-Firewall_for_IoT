import subprocess
import pipes
import os

class Passive_job():

    def __init__(self, pipe_name, cmd):
        self.pipe_name = pipe_name
        self.cmd = cmd
        self.pipe = pipes.Template()

    def launch(self):
        w_fd = self.pipe.open(self.pipe_name, 'w')
        self.popen = subprocess.Popen(self.cmd, stdout=w_fd)

    def stop(self):
        self.popen.terminate()
        if self.popen.poll() is None:
            self.popen.kill()
        self.pipe.reset()

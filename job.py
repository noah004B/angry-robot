import threading
from time import sleep
from pi_controller import PiController

class JobManager():
    def __init__(self, pi):
        self.thread = None
        self.pi = pi

    def run(self):
        if self.thread is None:
            return self.create_job()

        if not self.thread.is_alive():
            return self.create_job()

        return False

    def create_job(self):
        self.thread = Job(self.pi)
        self.thread.start()
        return True

class Job(threading.Thread):
    def __init__(self, pi):
        super(Job, self).__init__()
        self.pi = pi

    def run(self):
        try:
            print('-- Angry action start! --')
            self.angry_action()
        finally:
            print('-- Angry action end --')

    def angry_action(self):
        self.pi.mortar_on()
        for var in range(0, 80):
            self.pi.led_on()
            sleep(0.03)
            self.pi.led_off()
            sleep(0.03)
        self.pi.mortar_off()


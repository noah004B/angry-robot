import threading
from time import sleep
from pi_controller import PiController
from sound_controller import SoundController

class JobManager():
    def __init__(self, pi):
        self.angry_action_thread = None
        self.pi = pi
        self.sound = SoundController('chick-cry.mp3')

    def run(self):
        if self.angry_action_thread is None:
            return self.create_job()

        if not self.angry_action_thread.is_alive():
            return self.create_job()

        return False

    def create_job(self):
        self.angry_action_thread = AngryActionJob(self.pi, self.sound)
        self.angry_action_thread.start()
        return True

class AngryActionJob(threading.Thread):
    def __init__(self, pi, sound):
        super(AngryActionJob, self).__init__()
        self.pi = pi
        self.sound = sound

    def run(self):
        print('-- Angry action start! --')
        self.pi.mortar_on()
        self.sound.play()
        for var in range(0, 80):
            self.pi.led_on()
            sleep(0.03)
            self.pi.led_off()
            sleep(0.03)
        self.pi.mortar_off()
        self.sound.stop()
        print('-- Angry action end --')


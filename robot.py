import threading
# import enum

# @todo delete sleep
from datetime import datetime
from time import sleep

class Robot(threading.Thread):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        super(Robot, self).__init__()
        self.stop_event = threading.Event()

    def run(self):
        try:
            for _ in range(1000):
                print(f'{datetime.now():%H:%M:%S}')
                sleep(1)

                # 定期的にフラグを確認して停止させる
                if self.stop_event.is_set():
                    break
        finally:
            print('時間のかかる処理が終わりました\n')

    def angry(self):
        if not self.is_alive():
            self.start()
            return True
        else:
            return False

    def calm(self):
        if self.is_alive():
            self.stop_event.set()
            return True
        else:
            return False


from time import sleep
import threading
from datetime import datetime

class Scheduler:
    def __init__(self):
        self.fns = [] # Tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = datetime.now() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, datetime.now() * 1000 + n))
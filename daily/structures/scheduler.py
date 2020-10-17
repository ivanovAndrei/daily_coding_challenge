"""This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import threading
import time
import datetime

def f():
    print("Hello world, time now is {}".format(datetime.datetime.now()))

def _execute_job(f, interval):
    while(True):
        f()
        time.sleep(interval/1000.0)
        
class Scheduler():
    def __init__(self):
        """Nothing here so far."""
        self.threads = []

    def execute(self, f, interval_ms):
        t = threading.Thread(target=_execute_job, args=(f, interval_ms), daemon=True)
        t.start()
        self.threads.append(t)

s = Scheduler()
s.execute(f, 500)
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')
import time


class MeasuredScope:
    """A scope of the program that is measured in time"""

    def __init__(self, label):
        self.label = label
        self.start_time = time.time()

    def __del__(self):
        now = time.time()
        print(f'{self.label} time - {now - self.start_time:.2f}')
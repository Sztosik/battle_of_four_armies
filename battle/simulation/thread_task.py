import threading
from abc import ABC, abstractmethod


class ThreadTask(ABC):

    def __init__(self):
        self.task_end = threading.Event()

        self.task_thread = threading.Thread(
            name=self.__class__.__name__,
            target=self._run,
        )

    def start(self):
        self.task_thread.start()

    def stop(self):
        self.task_end.set()
        self.task_thread.join()

    @abstractmethod
    def _run(self):
        """Runs the thread"""

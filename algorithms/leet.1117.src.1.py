from threading import Lock

class H2O:
    def __init__(self):
        self.h = 0
        self.o = 0
        self.lockH = Lock()
        self.lockO = Lock()

    def release(self):
        if self.h != 2 or self.o != 1:
            return
        self.h = 0
        self.o = 0
        self.lockH.release()
        self.lockO.release()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lockH:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.h += 1
        if self.h >= 2:
            self.lockH.acquire()
        self.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lockO:
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            self.o += 1
        if self.o >= 1:
            self.lockO.acquire()
        self.release()

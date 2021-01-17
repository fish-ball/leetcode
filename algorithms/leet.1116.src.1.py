from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.k = 1
        self.lock0 = Lock()
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        print('zero')
        for i in range(self.n):
            with self.lock0:
                printNumber(0)
            self.lock0.acquire()
            if self.k % 2 == 1:
                self.lock1.release()
            else:
                self.lock2.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        print('even')
        for i in range(2, self.n + 1, 2):
            with self.lock2:
                printNumber(i)
                self.k += 1
            self.lock2.acquire()
            self.lock0.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        print('odd')
        for i in range(1, self.n + 1, 2):
            with self.lock1:
                printNumber(i)
                self.k += 1
            self.lock1.acquire()
            self.lock0.release()

from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.k = 0
        self.lockA = Lock()
        self.lockB = Lock()
        self.lockC = Lock()
        self.lockD = Lock()
        self.lockB.acquire()
        self.lockC.acquire()
        self.lockD.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(1, self.n+1):
            with self.lockA:
                if not i % 3 and i % 5:
                    printFizz()
            self.lockA.acquire()
            self.lockB.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(1, self.n+1):
            with self.lockB:
                if i % 3 and not i % 5:
                    printBuzz()
            self.lockB.acquire()
            self.lockC.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
    	for i in range(1, self.n+1):
            with self.lockC:
                if not i % 3 and not i % 5:
                    printFizzBuzz()
            self.lockC.acquire()
            self.lockD.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
    	for i in range(1, self.n+1):
            with self.lockD:
                if i % 3 and i % 5:
                    printNumber(i)
            self.lockD.acquire()
            self.lockA.release()

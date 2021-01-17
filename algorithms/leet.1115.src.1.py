from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            print(f'>> foo {i}')
            
            # printFoo() outputs "foo". Do not change or remove this line.
            with self.lock1:
                printFoo()
                
            self.lock1.acquire()
            self.lock2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            print(f'>> bar {i}')
            
            # printBar() outputs "bar". Do not change or remove this line.
            with self.lock2:
                printBar()
                
            self.lock2.acquire()
            self.lock1.release()

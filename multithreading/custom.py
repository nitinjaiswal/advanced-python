import threading
import time


class MyThread(threading.Thread):
    """Custom class to define the functionality of the thread.
    It over
    """
    def __init__(self, name, repeat):
        threading.Thread.__init__(self)
        self.name = name
        self.repeat = repeat

    def run(self):
        print(self.name + " starts")
        inc = 1
        while inc <= self.repeat:
            time.sleep(4)
            print(self.name + " : executes " + str(inc))
            inc += 1
        print(self.name + " ends")


def main():
    thread1 = MyThread("Thread1", 3)
    thread2 = MyThread("Thread2", 4)
    thread1.start()
    thread2.start()
    print(thread1.getName())
    thread2.getName()

    print("Main complete")

if __name__ == "__main__":
    main()
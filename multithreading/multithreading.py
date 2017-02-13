from threading import Thread
import time


def task(name, repeat):
    """Function which contains task performed by the thread
    """
    print(name + " starts")
    inc = 1
    while inc <= repeat:
        time.sleep(4)
        print(name + " : execution " + str(inc))
        inc += 1
    print(name + " ends")


def main():
    thread1 = Thread(target=task, args=("Thread1", 3))
    thread2 = Thread(target=task, args=("Thread2", 4))
    thread1.start()
    thread2.start()

    print("Main complete")

if __name__ == "__main__":
    main()

import queue
import threading
import time
import platform


def producer(data_que):
    while True:
        for i in range(2):
            time.sleep(1)
            data_que.put(i)


def consumer(data_que):
    while True:
        try:
            element = data_que.get()
            print(element)
        except IndexError as e:
            time.sleep(1)


if __name__ == "__main__":
    print(platform.python_implementation())
    q = queue.Queue()
    producer_thread = threading.Thread(target=producer, args=(q,))
    producer_thread.start()
    consumer_thread = threading.Thread(target=consumer, args=(q,))
    consumer_thread.start()

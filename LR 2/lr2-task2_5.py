import threading
import time

def set_event(event):
    while True:
        time.sleep(1)
        event.set()

def wait_for_event(event):
    print("Thread 2: Waiting for event to occur.")
    event.wait()
    print("Thread 2: Event occurred.")

def check_event_status(event):
    while not event.is_set():
        time.sleep(1)
        print("Thread 3: Event did not occur.")
    print("Thread 3: Stopping as event occurred.")

if __name__ == "__main__":
    # Создать объект события
    event = threading.Event()

    # Создайте три потока
    thread1 = threading.Thread(target=set_event, args=(event,))
    thread2 = threading.Thread(target=wait_for_event, args=(event,))
    thread3 = threading.Thread(target=check_event_status, args=(event,))

    # Запуск потоков
    thread1.start()
    thread2.start()
    thread3.start()

    thread3.join()

    thread1.join()
    thread2.join()

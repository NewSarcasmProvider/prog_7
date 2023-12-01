import threading
import time

class CustomQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.RLock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)
            print(f"Enqueued: {item}")
            time.sleep(1)
    def dequeue(self):
        with self.lock:
            if self.queue:
                item = self.queue.pop(0)
                print(f"Dequeued: {item}")
                time.sleep(1) 
                return item
            else:
                print("Queue is empty.")
                return None

def producer(queue):
    for i in range(5):
        queue.enqueue(f"Item {i}")

def consumer(queue):
    for _ in range(5):
        item = queue.dequeue()
        if item is not None:
            print(f"Processed: {item}")

if __name__ == "__main__":
    custom_queue = CustomQueue()

    thread_producer = threading.Thread(target=producer, args=(custom_queue,))
    thread_consumer = threading.Thread(target=consumer, args=(custom_queue,))

    thread_producer.start()
    thread_consumer.start()

    thread_producer.join()
    thread_consumer.join()

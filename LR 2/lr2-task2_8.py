import os
import threading

class FileSearchThread(threading.Thread):
    def __init__(self, directory, file_template, result_queue, lock):
        super(FileSearchThread, self).__init__()
        self.directory = directory
        self.file_template = file_template
        self.result_queue = result_queue
        self.lock = lock

    def run(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if self.file_template in file:
                    with self.lock:
                        if not self.result_queue.full():
                            self.result_queue.put(os.path.join(root, file))
                            print(f"Found file: {os.path.join(root, file)}")
                            return

def parallel_file_search(directory, file_template, num_threads):
    result_queue = threading.Queue()
    lock = threading.Lock()

    threads = []
    for _ in range(num_threads):
        thread = FileSearchThread(directory, file_template, result_queue, lock)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    directory_to_search = "/path/to/search"
    template_to_search = "example" 
    number_of_threads = 4 

    parallel_file_search(directory_to_search, template_to_search, number_of_threads)

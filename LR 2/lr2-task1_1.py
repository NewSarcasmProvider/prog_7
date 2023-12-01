import threading

# Определите функцию, которая будет выполняться каждым потоком
def thread_function():
    thread_name = threading.current_thread().name
    print(f"Поток {thread_name} запущен.")

# Создайте и запустите несколько потоков
num_threads = 5
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=thread_function)
    threads.append(thread)
    thread.start()

# Дождитесь завершения всех потоков
for thread in threads:
    thread.join()

print("Все потоки завершены.")
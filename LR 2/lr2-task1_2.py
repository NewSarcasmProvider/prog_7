import requests
import threading

upload_url = "https://example.com/"
file_paths = ["file1.jpg", "file2.png", "file3.txt"]

def upload_file(file_path):
    with open(file_path, "rb") as file:
        files = {"file": (file_path, file)}
        response = requests.post(upload_url, files=files)
        print(f"Uploaded {file_path}. Response: {response.status_code}")

# Создайте и запустите несколько потоков для загрузки
threads = []

for file_path in file_paths:
    thread = threading.Thread(target=upload_file, args=(file_path,))
    threads.append(thread)
    thread.start()

# Дождитесь завершения всех потоков
for thread in threads:
    thread.join()

print("Все файлы были загружены.")

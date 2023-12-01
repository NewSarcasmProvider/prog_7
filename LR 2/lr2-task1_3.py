import requests
import threading

request_urls = ["https://example.com/api/endpoint1", "https://example.com/api/endpoint2"]

def perform_streaming_request(url):
    with requests.get(url, stream=True) as response:
        if response.status_code == 200:
            print(f"Request for {url} succeeded")
        else:
            print(f"Request for {url} failed. Status code: {response.status_code}")

# Создайте и запустите несколько потоков для потоковых запросов
threads = []

for url in request_urls:
    thread = threading.Thread(target=perform_streaming_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все запросы на потоковую передачу были выполнены")

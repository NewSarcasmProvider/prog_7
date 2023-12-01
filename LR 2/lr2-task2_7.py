import threading
import time

def server(barrier):
    print("Server: Initializing...")
    time.sleep(2)
    print("Server: Ready.")
    barrier.wait()
    print("Server: Handling requests.")

def client(barrier):
    print("Client: Waiting for the server to be ready.")
    barrier.wait() 
    print("Client: Sending request to the server.")

if __name__ == "__main__":
    barrier = threading.Barrier(2)

    thread_server = threading.Thread(target=server, args=(barrier,))
    thread_client = threading.Thread(target=client, args=(barrier,))

    thread_server.start()

    thread_client.start()

    thread_server.join()
    thread_client.join()

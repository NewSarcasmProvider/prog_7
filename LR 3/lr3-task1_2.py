import asyncio
import datetime
from termcolor import colored
from pynput import keyboard

async def display_time():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        colored_time = colored(f"Current Time: {current_time}", 'green')
        print(colored_time, end='\r')
        await asyncio.sleep(1)

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            print("\nExiting the program.")
            loop.stop()
    except Exception as e:
        print(f"Error: {e}")

async def main():
    loop = asyncio.get_event_loop()
    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), loop.stop)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    await display_time()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

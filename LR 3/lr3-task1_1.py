import asyncio
import signal
import datetime

async def display_time():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current Time: {current_time}")
        await asyncio.sleep(1)

async def main():
    loop = asyncio.get_event_loop()
    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), loop.stop)

    await display_time()

if __name__ == "__main__":
    asyncio.run(main())

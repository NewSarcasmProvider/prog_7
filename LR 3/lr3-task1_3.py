import asyncio

async def task_one():
    print("Task One: Start")
    await asyncio.sleep(3)
    result = "Task One Result"
    print("Task One: End")
    return result

async def task_two():
    print("Task Two: Start")
    await asyncio.sleep(2)
    result = "Task Two Result"
    print("Task Two: End")
    return result

def process_results(results):
    for result in results:
        print(f"Processing Result: {result}")

async def main():
    results = await asyncio.gather(task_one(), task_two())

    while True:
        process_results(results)
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

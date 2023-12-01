import concurrent.futures
import asyncio

async def write_to_file(file_path, data, future):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data written to file: {file_path}")
        future.set_result(True)
    except Exception as e:
        future.set_exception(e)

async def read_from_file(file_path, future):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        print(f"Data read from file: {file_path}")
        future.set_result(data)
    except Exception as e:
        future.set_exception(e)

async def main():
    file_path = "example.txt"
    data_to_write = "Hello, this is some data to write to the file."

    # Используйте asyncio.Future, чтобы сигнализировать о завершении операций записи и чтения
    write_future = asyncio.Future()
    read_future = asyncio.Future()

    # Создайте ThreadPoolExecutor для параллельного выполнения задач записи и чтения
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Запустите задачи записи и чтения
        write_task = asyncio.ensure_future(write_to_file(file_path, data_to_write, write_future))
        read_task = asyncio.ensure_future(read_from_file(file_path, read_future))

        # Дождитесь завершения задач записи и чтения
        await asyncio.gather(write_task, read_task)

        # Получаем результаты из futures
        write_success = write_future.result()
        read_data = read_future.result()

        if write_success:
            print(f"Successfully wrote data to file: {file_path}")
            print(f"Read data from file: {file_path} -> {read_data}")

if __name__ == "__main__":
    # Запустите цикл событий
    asyncio.run(main())

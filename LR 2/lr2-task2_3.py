import asyncio
import concurrent.futures
import aiohttp
from pathlib import Path

async def download_image(session, url, sem, output_folder):
    async with sem:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                filename = Path(url).name
                filepath = output_folder / filename
                with open(filepath, 'wb') as f:
                    f.write(content)
                print(f"Downloaded: {url} -> {filepath}")
            else:
                print(f"Failed to download {url}. Status code: {response.status}")

async def main():
    urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
    ]

    output_folder = Path("downloaded_images")
    output_folder.mkdir(exist_ok=True)

    semaphore_limit = 2
    sem = asyncio.Semaphore(semaphore_limit)

    async with aiohttp.ClientSession() as session:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
            # Создать список задач
            tasks = [
                asyncio.ensure_future(download_image(session, url, sem, output_folder))
                for url in urls
            ]

            # Собираем и ждем завершения всех задач
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Запускаем цикл событий
    asyncio.run(main())

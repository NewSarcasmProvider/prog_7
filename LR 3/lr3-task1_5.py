import aiohttp
import asyncio

class WebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def fetch_data(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape_pages(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_data(session, url) for url in self.urls]
            results = await asyncio.gather(*tasks)
            return results

async def handle_request(request):
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file]

    scraper = WebScraper(urls)
    data = await scraper.scrape_pages()

    return aiohttp.web.json_response({"data": data})

async def main():
    app = aiohttp.web.Application()
    app.router.add_get('/', handle_request)

    runner = aiohttp.web.AppRunner(app)
    await runner.setup()

    site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started on http://localhost:8080")

    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        pass
    finally:
        await runner.cleanup()

if __name__ == "__main__":
    asyncio.run(main())

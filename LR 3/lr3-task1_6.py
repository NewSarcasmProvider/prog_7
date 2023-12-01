import aiohttp
import asyncio

class WebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()

    async def fetch_data(self, url):
        async with self.session.get(url) as response:
            return await response.text()

    async def scrape_pages(self):
        tasks = [self.fetch_data(url) for url in self.urls]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file]

    async with WebScraper(urls) as scraper:
        data = await scraper.scrape_pages()

    print("Scraped data:", data)

if __name__ == "__main__":
    asyncio.run(main())

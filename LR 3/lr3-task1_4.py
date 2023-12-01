import asyncio
import aiohttp
import asyncpg
import json

WEB_SERVER_URL = "https://rnacentral.org/api/v1/rna/"
DB_CONNECTION_STRING = "postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"

async def fetch_web_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def fetch_database_data(connection_string):
    async with asyncpg.connect(connection_string) as connection:
        query = "SELECT * FROM your_table_name;"
        result = await connection.fetch(query)
        return result

def process_results(web_data, database_data):
    print("Web Server Data:")
    print(json.dumps(web_data, indent=2))

    print("\nDatabase Data:")
    for row in database_data:
        print(row)

async def main():
    web_task = fetch_web_data(WEB_SERVER_URL)
    db_task = fetch_database_data(DB_CONNECTION_STRING)

    web_data, database_data = await asyncio.gather(web_task, db_task)

    process_results(web_data, database_data)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

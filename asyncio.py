import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'

async def fetch(session, url):
    with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])

async def fetch1(session, url):
    with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])

async def fetchBoth(str, session, URL):
    print(str)
    await fetch(session, URL)
    await fetch1(session, URL)

async def main():
    start = time.time()
    ##
    with aiohttp.ClientSession() as session:
        tasks = [fetchBoth("Hello", session, URL) for i in range(100)]
        await asyncio.gather(*tasks)
    ##
    end = time.time()
    print("Total time taken = " + str(end-start))

if __name__ == "__main__":
    asyncio.run(main())
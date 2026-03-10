import aiohttp
import asyncio

class HTTPEngine:

    def __init__(self, timeout=10, concurrency=50):
        self.timeout = timeout
        self.semaphore = asyncio.Semaphore(concurrency)
        self.session = None

    async def start(self):
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        self.session = aiohttp.ClientSession(timeout=timeout)

    async def close(self):
        if self.session:
            await self.session.close()

    async def get(self, url):

        async with self.semaphore:
            try:
                async with self.session.get(url) as response:
                    text = await response.text()
                    return response.status, text, response.headers

            except:
                return None, None, None
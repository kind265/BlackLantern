import asyncio
from core.logger import success

async def run(target):
    await asyncio.sleep(1)
    success(f"Test module scanned {target}")
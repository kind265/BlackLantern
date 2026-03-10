import asyncio
from core.logger import info

PORTS = [21,22,25,80,443]

async def grab(target, port):

    try:

        reader, writer = await asyncio.open_connection(target, port)

        writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
        await writer.drain()

        data = await asyncio.wait_for(reader.read(1024), timeout=2)

        info(f"Banner {port}: {data.decode(errors='ignore').splitlines()[0]}")

        writer.close()
        await writer.wait_closed()

    except:
        pass


async def run(target):

    tasks = []

    for port in PORTS:
        tasks.append(grab(target, port))

    await asyncio.gather(*tasks)
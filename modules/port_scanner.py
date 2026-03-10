import asyncio
from core.logger import success, info

FAST_PORTS = [
21,22,23,25,53,80,110,135,139,143,
443,445,3306,3389,8080
]

PRO_PORTS = list(range(1,1001))

ELITE_PORTS = list(range(1,65536))


async def scan_port(target, port):

    try:
        conn = asyncio.open_connection(target, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)

        success(f"Port {port} OPEN")

        writer.close()
        await writer.wait_closed()

    except:
        pass


async def run(target, mode="fast"):

    if mode == "fast":
        ports = FAST_PORTS
        info("Running FAST port scan")

    elif mode == "pro":
        ports = PRO_PORTS
        info("Running PRO port scan (1000 ports)")

    elif mode == "elite":
        ports = ELITE_PORTS
        info("Running ELITE port scan (65535 ports)")

    tasks = []

    for port in ports:
        tasks.append(scan_port(target, port))

    await asyncio.gather(*tasks)
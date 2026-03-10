import asyncio
from core.logger import success, info

WORDLIST = "wordlists/common.txt"

async def check(http, kb, target, word):

    url = f"{target}/{word}"

    status, _, _ = await http.get(url)

    if status in [200,301,302,403]:

        success(f"Discovered: {url} ({status})")

        kb.add_endpoint(url)

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    info("Starting content discovery")

    with open(WORDLIST) as f:
        words = [line.strip() for line in f]

    tasks = []

    for word in words:
        tasks.append(check(http, kb, target, word))

    await asyncio.gather(*tasks)
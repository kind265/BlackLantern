from bs4 import BeautifulSoup
from urllib.parse import urljoin
from core.logger import info

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    info("Starting web crawler")

    status, text, headers = await http.get(target)

    if not text:
        return

    soup = BeautifulSoup(text, "html.parser")

    for link in soup.find_all("a"):

        href = link.get("href")

        if href:
            full = urljoin(target, href)

            kb.add_endpoint(full)

            info(f"Discovered endpoint: {full}")
from core.logger import warning

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    url = f"{target}/.git/config"

    status, text, headers = await http.get(url)

    if status == 200:

        warning("Public Git repository exposed")

        kb.add_vulnerability({
            "type": "Git Exposure",
            "url": url
        })
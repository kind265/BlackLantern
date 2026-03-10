from core.logger import warning

FILES = [
"backup.zip",
"backup.tar.gz",
"database.sql",
"site.bak",
"config.bak"
]

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    for file in FILES:

        url = f"{target}/{file}"

        status, text, headers = await http.get(url)

        if status == 200:

            warning(f"Exposed backup found: {url}")

            kb.add_vulnerability({
                "type": "Backup Exposure",
                "url": url
            })
from core.logger import success

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    status, text, headers = await http.get(target)

    if not headers:
        return

    if "Server" in headers:
        success(f"Server: {headers['Server']}")

    if "X-Powered-By" in headers:
        success(f"Technology: {headers['X-Powered-By']}")

        kb.add_technology("X-Powered-By", headers["X-Powered-By"])
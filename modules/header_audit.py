from core.logger import warning

SECURITY_HEADERS = [
"X-Frame-Options",
"Content-Security-Policy",
"X-XSS-Protection"
]

async def run(target, http, kb, mode):

    if not target.startswith("http"):
        target = "http://" + target

    status, text, headers = await http.get(target)

    if not headers:
        return

    for header in SECURITY_HEADERS:

        if header not in headers:

            warning(f"Missing security header: {header}")
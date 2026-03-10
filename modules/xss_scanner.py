from core.logger import warning

payload = "<script>alert(1)</script>"

async def run(target, http, kb, mode):

    endpoints = kb.get_endpoints()

    for url in endpoints:

        if "?" in url:

            test = url + payload

            status, text, headers = await http.get(test)

            if payload in (text or ""):

                warning(f"Possible XSS: {url}")

                kb.add_vulnerability({
                    "type": "XSS",
                    "url": url
                })
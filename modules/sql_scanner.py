from core.logger import warning

payload = "'"

async def run(target, http, kb, mode):

    endpoints = kb.get_endpoints()

    for url in endpoints:

        if "?" in url:

            test_url = url + payload

            status, text, headers = await http.get(test_url)

            if text and "sql" in text.lower():

                warning(f"Possible SQL Injection: {url}")

                kb.add_vulnerability({
                    "type": "SQL Injection",
                    "url": url
                })
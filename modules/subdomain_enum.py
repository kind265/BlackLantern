import dns.resolver
from core.logger import info, success

WORDLIST = "wordlists/subdomains.txt"

async def run(target, http, kb, mode):

    info("Starting subdomain enumeration")

    with open(WORDLIST) as f:
        subs = [line.strip() for line in f]

    domain = target.replace("http://","").replace("https://","")

    for sub in subs:

        test = f"{sub}.{domain}"

        try:
            dns.resolver.resolve(test, "A")

            success(f"Subdomain discovered: {test}")

            kb.add_endpoint("http://" + test)

        except:
            pass
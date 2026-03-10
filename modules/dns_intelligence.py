import dns.resolver
from core.logger import info

async def run(target, http, kb, mode):

    domain = target.replace("http://","").replace("https://","")

    info("Collecting DNS records")

    for record in ["MX","TXT","NS"]:

        try:
            answers = dns.resolver.resolve(domain, record)

            for r in answers:
                info(f"{record}: {r}")

        except:
            pass
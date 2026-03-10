import sys
import asyncio
from core.engine import ScanEngine
from core.target_parser import parse_target
from core.logger import info, error

def banner():
    print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝
██╔══██╗██║     ██╔══██║██║     ██╔═██╗
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

BlackLantern Vulnerability Scanner
""")

async def main():

    banner()

    if len(sys.argv) < 3:
        error("Usage: python main.py scan <target> [--ports|--full] [--fast|--pro|--elite]")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    args = sys.argv[3:]

    modules = None
    mode = "fast"

    # MODULE FLAGS
    if "--ports" in args:
        modules = ["port_scanner"]

    if "--web" in args:
        modules = ["web_crawler", "tech_detector", "web_vuln_scanner"]

    if "--full" in args:
        modules = None

    # SCAN MODE FLAGS
    if "--fast" in args:
        mode = "fast"

    if "--pro" in args:
        mode = "pro"

    if "--elite" in args:
        mode = "elite"

    if command == "scan":

        parsed = parse_target(target)
        info(f"Target detected: {parsed['type']}")
        info(f"Scan mode: {mode}")

        engine = ScanEngine(target, modules, mode)
        await engine.start()

if __name__ == "__main__":
    asyncio.run(main())
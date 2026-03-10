import asyncio
from core.logger import info
from core.module_loader import load_modules
from network.http_engine import HTTPEngine
from intelligence.knowledge_base import KnowledgeBase

class ScanEngine:

    def __init__(self, target, modules=None, mode="fast"):

        self.target = target
        self.mode = mode
        self.modules = load_modules(modules)

        self.http = HTTPEngine()
        self.kb = KnowledgeBase()

    async def run_module(self, module):

        if hasattr(module, "run"):
            await module.run(self.target, self.http, self.kb, self.mode)

    async def start(self):

        info(f"Starting scan on {self.target}")

        await self.http.start()

        tasks = []

        for module in self.modules:
            tasks.append(self.run_module(module))

        await asyncio.gather(*tasks)

        await self.http.close()
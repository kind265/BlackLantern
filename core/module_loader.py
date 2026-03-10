import importlib
import os

MODULE_PATH = "modules"

def load_modules(selected=None):
    modules = []

    for file in os.listdir(MODULE_PATH):
        if file.endswith(".py"):
            name = file[:-3]

            if selected and name not in selected:
                continue

            module = importlib.import_module(f"{MODULE_PATH}.{name}")
            modules.append(module)

    return modules
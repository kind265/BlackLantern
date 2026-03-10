import re

def parse_target(target):
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", target):
        return {"type": "ip", "value": target}

    elif "." in target:
        return {"type": "domain", "value": target}

    else:
        return {"type": "unknown", "value": target}
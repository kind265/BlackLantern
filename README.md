# BlackLantern

BlackLantern is a modular command‑line vulnerability assessment and reconnaissance framework written in Python. It is designed for security researchers, students, and ethical hackers who want a flexible scanning platform that combines multiple security capabilities into a single tool.

The project focuses on **modular architecture, asynchronous scanning, and extensibility**, allowing new modules to be added easily as plugins.

---

# Features

## Network Intelligence

* Async port scanning (Fast / Pro / Elite modes)
* Banner grabbing
* Service discovery

## Web Intelligence

* Website crawling
* Content discovery using wordlists
* Technology detection
* Security header auditing

## Vulnerability Detection

* Basic SQL injection detection
* Reflected XSS detection
* Missing security header checks

## Attack Surface Recon

* Subdomain enumeration
* DNS record collection
* Backup file exposure detection
* Public Git repository exposure

## Core Framework

* Asynchronous scanning engine
* Shared HTTP request engine
* Knowledge base for module collaboration
* Modular plugin architecture

---

# Architecture

BlackLantern is built around a modular scanning engine where each module performs a specific security task.

```
BlackLantern/

core/
  engine.py
  module_loader.py
  target_parser.py
  logger.py

network/
  http_engine.py

intelligence/
  knowledge_base.py

modules/
  port_scanner.py
  web_crawler.py
  content_discovery.py
  tech_detector.py
  sql_scanner.py
  xss_scanner.py
  header_audit.py
  subdomain_enum.py
  dns_intelligence.py
  backup_finder.py
  git_exposure.py

wordlists/
  common.txt
  subdomains.txt

main.py
```

Modules communicate through a **central knowledge base**, allowing discoveries from one module to be reused by others.

Example:

* crawler finds endpoints
* SQL scanner tests those endpoints
* XSS scanner analyzes the same parameters

---

# Installation

## 1. Clone the repository

```
git clone https://github.com/kind265/BlackLantern.git
cd BlackLantern
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

Example dependencies:

```
aiohttp
requests
beautifulsoup4
dnspython
rich
colorama
```

---

# Usage

Basic scan:

```
python main.py scan example.com
```

Port scanning:

```
python main.py scan example.com --ports
```

Full reconnaissance scan:

```
python main.py scan example.com --full
```

Web‑focused scan:

```
python main.py scan example.com --web
```

Scan speed modes:

```
--fast   (common ports)
--pro    (top 1000 ports)
--elite  (full port range)
```

Example:

```
python main.py scan example.com --ports --pro
```

---

# Example Output

```
[INFO] Target detected: domain
[INFO] Starting scan on example.com

[INFO] Starting web crawler
[INFO] Discovered endpoint: /login
[INFO] Discovered endpoint: /product?id=1

Server: nginx
Technology: PHP

[WARNING] Missing security header: X-Frame-Options
[WARNING] Possible SQL Injection: /product?id=1
```

---

# Design Goals

BlackLantern was designed with the following goals:

* modular security framework
* high performance asynchronous scanning
* simple CLI interface
* extensibility for research and experimentation

The project can be expanded with additional modules for:

* advanced vulnerability detection
* OSINT intelligence
* reporting engines
* automation pipelines

---

# Ethical Use

BlackLantern is intended **only for educational purposes and authorized security testing**.

Do not scan systems without permission. Always follow responsible disclosure practices and the laws applicable in your country.

---

# Contributing

Contributions are welcome.

To add a new module:

1. Create a new file in `modules/`
2. Implement a `run(target, http, kb, mode)` function
3. The engine will automatically load the module

Example module template:

```python
async def run(target, http, kb, mode):
    pass
```

# Author

Created by **Hopeson Chikuse**.

Cybersecurity enthusiast building open security tools and research projects.

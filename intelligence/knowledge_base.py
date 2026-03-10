class KnowledgeBase:

    def __init__(self):

        self.endpoints = set()
        self.technologies = {}
        self.vulnerabilities = []

    def add_endpoint(self, url):
        self.endpoints.add(url)

    def add_technology(self, key, value):
        self.technologies[key] = value

    def add_vulnerability(self, vuln):
        self.vulnerabilities.append(vuln)

    def get_endpoints(self):
        return list(self.endpoints)
class ProxyRequest:
    """Equation of state element"""

    def __init__(self):
        self.name = ""
        self.type = ""
        self.payload = {}

    def __str__(self) -> str:
        return "name: {}\ntype: {}".format(self.name, self.type)
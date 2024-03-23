class ProxyRequest:
    """Equation of state element"""
    name: str
    type: str
    payload: dict

    def __str__(self) -> str:
        return "name: {}\ntype: {}".format(self.name, self.type)
# Definição de cada entrada na tabela de símbolos

class SymbolTableData:

    def __init__(self, type, address) -> None:
        self.type = type
        self.address = address

    def to_string(self):
        return '[type: {}, addr: {}]'.format(self.type, self.address)
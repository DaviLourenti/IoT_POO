class IoT_Item:
    def __init__(self, local: str, tipo: str, conectividade: str) -> None:
        self.local = local
        self.tipo = tipo
        self.conectividade = conectividade

    def imprimir_informações(self) -> str:
        return f"""
        conectividade: {self.conectividade}
        tipo: {self.tipo}
        local: {self.local}"""




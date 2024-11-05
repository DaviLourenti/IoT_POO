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



class IoT_Monitor(IoT_Item):
    def __init__(self, consumo: float, local: str,  estado: str, tipo: str, conectividade: str) -> None:
        self.consumo = consumo
        self.estado = estado
        super().__init__(local, tipo, conectividade)

    def imprimir_informações(self) -> str:
        super().imprimir_informações()
        return f"""
        consumo: {self.consumo}
        estado: {self.estado}

        """
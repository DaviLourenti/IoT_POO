from classe_IoT_Item import IoT_Item

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
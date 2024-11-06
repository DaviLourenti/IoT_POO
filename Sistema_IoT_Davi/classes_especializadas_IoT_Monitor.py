from classe_IoT_Monitor import IoT_Monitor

class Janela(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str):
        super().__init__(consumo, local, estado, tipo, conectividade)



class Porta(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str, status: str):
        super().__init__(consumo, local, estado, tipo, conectividade)
        self.status = status

    def imprimir_informações(self) -> str:
        super().imprimir_informações()
        return f"""
        status: {self.status}
        """



class Camera(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str):
        super().__init__(consumo, local, estado, tipo, conectividade)

    def ver_camera(self):
        pass

from Sistema_IoT_Davi.classes_paternas import IoT_Monitor



class JanelaMonitor(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str):
        super().__init__(consumo, local, estado, tipo, conectividade)



class PortaMonitor(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str, status: str):
        super().__init__(consumo, local, estado, tipo, conectividade)
        self.status = status

    def imprimir_informações(self) -> str:
        super().imprimir_informações()
        return f"""
        status: {self.status}
        """



class CameraMonitor(IoT_Monitor):
    def __init__(self, consumo: float, local: str, estado: str, tipo: str, conectividade: str):
        super().__init__(consumo, local, estado, tipo, conectividade)

    def ver_camera(self):
        pass

class RepartoDiario:
    def __init__(self, fecha):
        self.fecha = fecha
        self.remitosVenta = []
        self.totalReparto = 0.0

    def agregar_remito(self, remito):
        if not remito.detallesRemito:
            raise ValueError(
                "El remito debe tener al menos un detalle."
            )

        self.remitosVenta.append(remito)
        self.calcular_total()

    def calcular_total(self):
        self.totalReparto = 0.0

        for remito in self.remitosVenta:
            self.totalReparto += remito.calcular_total()

        return self.totalReparto
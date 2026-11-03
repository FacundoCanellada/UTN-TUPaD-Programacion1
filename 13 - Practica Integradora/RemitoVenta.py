class RemitoVenta:
    def __init__(self, nombreCliente, numeroRemito):
        self.nombreCliente = nombreCliente
        self.numeroRemito = numeroRemito
        self.detallesRemito = []
        self.totalVenta = 0.0

    def agregar_detalle(self, detalle):
        self.detallesRemito.append(detalle)
        self.calcular_total()

    def calcular_total(self):
        self.totalVenta = 0.0

        for detalle in self.detallesRemito:
            self.totalVenta += detalle.subtotal

        return self.totalVenta
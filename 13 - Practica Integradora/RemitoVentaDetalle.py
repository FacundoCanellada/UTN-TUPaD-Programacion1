class RemitoVentaDetalle:
    def __init__(self, cantidad, articulo):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        self.cantidad = cantidad
        self.articulo = articulo
        self.subtotal = cantidad * articulo.precio
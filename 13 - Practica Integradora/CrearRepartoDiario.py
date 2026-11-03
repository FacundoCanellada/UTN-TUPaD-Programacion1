from Articulo import Articulo
from RemitoVentaDetalle import RemitoVentaDetalle
from RemitoVenta import RemitoVenta
from RepartoDiario import RepartoDiario


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("El texto no puede quedar vacío.")


def leer_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Ingresá un número entero.")
            continue

        if numero > 0:
            return numero

        print("El número debe ser mayor a cero.")


def confirmar(mensaje):
    while True:
        respuesta = input(
            f"{mensaje} (SI/NO): "
        ).strip().upper()

        if respuesta in ("SI", "SÍ", "S"):
            return True

        if respuesta in ("NO", "N"):
            return False

        print("Respondé SI o NO.")


def buscar_articulo(codigo, articulosDisponibles):
    for articulo in articulosDisponibles:
        if articulo.codigo == codigo:
            return articulo

    return None


def mostrar_reparto(reparto):
    reparto.calcular_total()

    print("\nReparto Diario")
    print(f"Fecha: {reparto.fecha}")
    print("\n-------------- Remitos del Reparto --------------")

    for remito in reparto.remitosVenta:
        print(f"\nNombre Cliente: {remito.nombreCliente}")
        print(f"Número Remito: {remito.numeroRemito}")

        print(
            f"{'Cantidad':>8} "
            f"{'Denominación Artículo':<30} "
            f"{'Precio Unitario':>15} "
            f"{'Subtotal':>12}"
        )

        for detalle in remito.detallesRemito:
            print(
                f"{detalle.cantidad:>8} "
                f"{detalle.articulo.denominacion:<30} "
                f"{detalle.articulo.precio:>15.2f} "
                f"{detalle.subtotal:>12.2f}"
            )

        print(f"Total Remito Venta: ${remito.totalVenta:.2f}")
        print("-" * 70)

    print(f"\nMonto Total Reparto: ${reparto.totalReparto:.2f}")


class CrearRepartoDiario:
    @staticmethod
    def main():
        articulosDisponibles = [
            Articulo("10", "Filtro de Aceite", 10000),
            Articulo("20", "Filtro de Aire", 8000),
            Articulo("30", "Filtro de Combustible", 7500),
            Articulo("40", "Aceite de Motor sw/10", 25000),
            Articulo("50", "Correa de Distribución", 20000),
        ]

        clientesReparto = {
            "20284569875": "Juan Alonso",
            "20157896542": "Emiliano Salas",
            "50258963654": "Pacallcar Autos",
            "27654987456": "Julieta Videla",
            "50335588945": "Todo Auto SRL",
        }

        fecha = leer_texto("Fecha del reparto: ")
        reparto = RepartoDiario(fecha)

        # Bucle de carga de remitos.
        while True:
            print("\nNUEVO REMITO")

            numero = leer_entero_positivo(
                "Número de remito: "
            )

            cuit = leer_texto("CUIT del cliente: ")

            if cuit in clientesReparto:
                nombreCliente = clientesReparto[cuit]
                print(f"Cliente: {nombreCliente}")
            else:
                nombreCliente = leer_texto(
                    "Cliente nuevo. Ingresá su razón social: "
                )
                clientesReparto[cuit] = nombreCliente

            remito = RemitoVenta(nombreCliente, numero)

            print("\nARTÍCULOS DISPONIBLES")

            for articulo in articulosDisponibles:
                print(
                    f"{articulo.codigo} - "
                    f"{articulo.denominacion} - "
                    f"${articulo.precio:.2f}"
                )

            # Bucle de carga de detalles.
            # La pregunta de salida aparece después del primer detalle.
            while True:

                # Repetir la búsqueda hasta ingresar un código válido.
                while True:
                    codigo = leer_texto(
                        "Código del artículo: "
                    )

                    articulo = buscar_articulo(
                        codigo, articulosDisponibles
                    )

                    if articulo is not None:
                        break

                    print(
                        "el código es incorrecto, ingrese nuevamente"
                    )

                cantidad = leer_entero_positivo(
                    "Cantidad: "
                )

                detalle = RemitoVentaDetalle(
                    cantidad, articulo
                )

                remito.agregar_detalle(detalle)

                print(
                    f"Subtotal del detalle: "
                    f"${detalle.subtotal:.2f}"
                )

                if not confirmar(
                    "¿Querés agregar otro detalle?"
                ):
                    break

            reparto.agregar_remito(remito)

            if not confirmar(
                "¿Querés agregar otro remito?"
            ):
                break

        mostrar_reparto(reparto)


if __name__ == "__main__":
    CrearRepartoDiario.main()
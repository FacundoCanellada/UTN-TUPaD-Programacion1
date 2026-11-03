"""Pruebas de reglas de negocio y recorridos por el menú interactivo."""

from contextlib import redirect_stdout
from io import StringIO
import unittest
from unittest.mock import patch

from TP10_POO_CanelladaFacundo import main
from entrada import leer_decimal
from ejercicio_1_matriz.celda import Celda
from ejercicio_1_matriz.matriz import Matriz
from ejercicio_2_notas.alumno import Alumno
from ejercicio_2_notas.nota import Nota
from ejercicio_3_restaurante.ingrediente import Ingrediente
from ejercicio_3_restaurante.plato import Plato
from ejercicio_4_computadoras.componente_cpu import ComponenteCPU
from ejercicio_4_computadoras.computadora import Computadora
from ejercicio_5_barrio.barrio import Barrio
from ejercicio_5_barrio.habitacion import Habitacion
from ejercicio_5_barrio.vivienda import Vivienda


class PruebasPOO(unittest.TestCase):
    def test_matriz_rechaza_coordenada_duplicada_sin_reemplazar_valor(self):
        matriz = Matriz()
        matriz.agregar_celda(Celda(0, 0, "hola"))
        matriz.agregar_celda(Celda(0, 1, "otra"))
        with self.assertRaises(ValueError):
            matriz.agregar_celda(Celda(0, 0, "duplicada"))
        self.assertEqual(matriz.obtener_valor(0, 0), "hola")
        self.assertEqual(len(matriz.celdasMatriz), 2)
        self.assertEqual(matriz.obtener_valor(9, 9),
                         "La fila y columna indicada no ha sido asignada en ninguna celda")

    def test_listas_independientes_entre_instancias(self):
        primera = Matriz()
        segunda = Matriz()
        primera.agregar_celda(Celda(1, 1, "A"))
        self.assertEqual(segunda.celdasMatriz, [])
        ana = Alumno("Ana", 1)
        juan = Alumno("Juan", 2)
        ana.agregar_nota(Nota("Programación", 8))
        self.assertEqual(juan.notas, [])

    def test_promedio_y_al_menos_una_nota(self):
        alumno = Alumno("Ana", 1)
        with self.assertRaises(ValueError):
            alumno.calcular_promedio()
        alumno.agregar_nota(Nota("Programación", 8))
        alumno.agregar_nota(Nota("Matemática", 9.5))
        self.assertEqual(alumno.calcular_promedio(), 8.75)

    def test_bebida_sin_ingredientes_y_plato_con_ingredientes(self):
        agua = Plato("Agua", 100, True)
        agua.validar_ingredientes()
        with self.assertRaises(ValueError):
            agua.agregar_ingrediente(Ingrediente("Limón", 1, "unidad"))
        pizza = Plato("Pizza", 450, False)
        with self.assertRaises(ValueError):
            pizza.validar_ingredientes()
        pizza.agregar_ingrediente(Ingrediente("Queso", 300, "gramos"))
        pizza.validar_ingredientes()

    def test_cotizacion_del_ejemplo_del_enunciado(self):
        computadora = Computadora("Lenovo", "X64K")
        for nombre, marca, cantidad, precio in [
            ("Placa Madre", "ASUS", 1, 16000),
            ("Procesador", "INTEL I7", 1, 20000),
            ("Memoria RAM 2Gb", "Kingston", 2, 8000),
            ("Disco Rígido", "WD SSD", 1, 7500),
        ]:
            computadora.agregar_componente(ComponenteCPU(nombre, marca, cantidad, precio))
        self.assertEqual(computadora.calcular_costo(), 59500)
        self.assertEqual(computadora.calcular_precio_venta(), 77350)

    def test_recargos_a_ambos_lados_del_limite_y_en_igualdad(self):
        for costo, factor in [(49999, 1.4), (50000, 1.3), (50001, 1.3)]:
            with self.subTest(costo=costo):
                computadora = Computadora("Marca", "Modelo")
                computadora.agregar_componente(ComponenteCPU("CPU", "Marca", 1, costo))
                self.assertAlmostEqual(computadora.calcular_precio_venta(), costo * factor)

    def test_superficies_totales_y_filtro_por_manzana(self):
        barrio = Barrio("Barrio", "Empresa")
        for numero, manzana, terreno, cubierta in [(1, "A", 200, 50), (2, "B", 150, 40), (3, "A", 100, 10)]:
            vivienda = Vivienda("Calle", numero, manzana, numero, terreno)
            vivienda.agregar_habitacion(Habitacion("Habitación", cubierta))
            barrio.agregar_vivienda(vivienda)
        self.assertEqual(barrio.getSuperficieTotalTerreno(), 450)
        self.assertEqual(barrio.getSuperficieTotalTerrenoXManzana("A"), 300)
        self.assertEqual(barrio.getSuperficieTotalTerrenoXManzana("Z"), 0)
        self.assertEqual(barrio.getSuperficieTotalCubierta(), 100)

    def test_superficie_cubierta_igual_o_mayor_al_terreno(self):
        vivienda = Vivienda("Calle", 1, "A", 1, 20)
        vivienda.agregar_habitacion(Habitacion("Cocina", 20))
        self.assertEqual(vivienda.getMetrosCuadradosCubiertos(), 20)
        vivienda.agregar_habitacion(Habitacion("Baño", 5))
        barrio = Barrio("Barrio", "Empresa")
        barrio.agregar_vivienda(vivienda)
        with self.assertRaisesRegex(ValueError, "La superficie cubierta no puede ser mayor a la superficie del terreno"):
            barrio.getSuperficieTotalCubierta()

    def test_entrada_decimal_reintenta_ante_texto_nan_infinito_y_cero(self):
        with patch("builtins.input", side_effect=["texto", "nan", "inf", "0", "2,5"]), redirect_stdout(StringIO()):
            self.assertEqual(leer_decimal("Cantidad: ", incluir_minimo=False), 2.5)

    def ejecutar_menu(self, entradas):
        salida = StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            main()
        return salida.getvalue()

    def test_menu_matriz_con_duplicado_y_consulta(self):
        salida = self.ejecutar_menu(["1", "hola", "0", "0", "otro", "0", "0", "FIN", "SI", "0", "0", "NO", "0"])
        self.assertIn("Ya existe una celda", salida)
        self.assertIn("Valor: hola", salida)

    def test_menu_notas_con_dos_notas(self):
        salida = self.ejecutar_menu(["2", "Ana", "1", "Matemática", "8", "SI", "Programación", "10", "NO", "NO", "0"])
        self.assertIn("Promedio: 9.00", salida)

    def test_menu_bebida_y_comida(self):
        salida = self.ejecutar_menu(["3", "Agua", "100", "SI", "SI", "Pizza", "450", "NO", "Queso", "300", "gramos", "NO", "NO", "0"])
        self.assertIn("Agua\nPrecio: $ 100.00", salida)
        self.assertIn("Queso", salida)

    def test_menu_permite_cotizar_dos_computadoras(self):
        salida = self.ejecutar_menu(["4", "Marca1", "Modelo1", "RAM", "Kingston", "2", "8000", "NO", "SI", "Marca2", "Modelo2", "CPU", "Intel", "1", "50000", "NO", "NO", "0"])
        self.assertIn("$ 22400.00", salida)
        self.assertIn("$ 65000.00", salida)

    def test_menu_demostracion_barrio(self):
        salida = self.ejecutar_menu(["5", "0"])
        self.assertIn("Terreno total: 350.00", salida)
        self.assertIn("Superficie cubierta del barrio: 90.00", salida)
        self.assertIn("Validación esperada", salida)


if __name__ == "__main__":
    unittest.main()

import unittest
from .funcs import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    def test_emisiones_por_defecto(self):
        consumo_kwh = 20
        emision_por_defecto = 0.4

        resultado_esperado = consumo_kwh * emision_por_defecto
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh), resultado_esperado)

    def test_emisiones_personalizada(self):
            consumo_kwh = 20
            emision_personalizada = 1.4
    
            resultado_esperado = consumo_kwh * emision_personalizada
            self.assertEqual(calcular_emisiones_carbono(consumo_kwh, emision_personalizada), resultado_esperado)

    
    def test_caso_limite(self):
        resultado_esperado = 0
        self.assertEqual(calcular_emisiones_carbono(0, 200), resultado_esperado)

    def test_decimales(self):
         resultado_esperado_aproximado = 4.4

         self.assertAlmostEqual(calcular_emisiones_carbono(1.1, 4), resultado_esperado_aproximado)


    def test_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-20)

    
         

    
            

from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(3, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)
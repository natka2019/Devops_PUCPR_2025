import unittest
import sys
import os
import pytest 

from src.calculadora import *

class TestCalculadora(unittest.TestCase):
    
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)
    
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(10, 15), -5)
    
    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 5), 20)
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(0, 100), 0)

    def test_dividir(self):
        self.assertEqual(dividir(20, 5), 4)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(100, 10), 10)

    def test_media(self):
        self.assertEqual(media(5, 5), 5)
        self.assertEqual(media(12, 18), 15)
        self.assertEqual(media(100, 500), 300)

if __name__ == '__main__':
    unittest.main()
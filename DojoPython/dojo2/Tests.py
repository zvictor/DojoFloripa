import unittest2
from CaixaEletronico import CaixaEletronico

class TesteDoCaixaEletronico(unittest2.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "TesteDoCaixaEletronico:"
        
    def setUp(self):
	self.caixa = CaixaEletronico()
        pass

    def test_saque_100(self):
        resultado = self.caixa.saque(100)
        self.assertEqual({100:1}, resultado)

    def test_saque_200(self):
	resultado = self.caixa.saque(200)
	self.assertEqual({100:2}, resultado)

    def test_saque_150(self):
	resultado = self.caixa.saque(150)
	self.assertEqual({100:1, 50:1}, resultado)

    def test_saque_170(self):
	resultado = self.caixa.saque(170)
	self.assertEqual({100:1, 50:1, 20:1}, resultado)

    def test_saque_20(self):
	resultado = self.caixa.saque(20)
	self.assertEqual({20:1}, resultado)

    def test_saque_10(self):
	resultado = self.caixa.saque(10)
	self.assertEqual({10:1}, resultado)

    def test_saque_170(self):
	caixa2 = CaixaEletronico({100: 1, 20:5, 10:10})
	resultado = caixa2.saque(170)
	self.assertEqual({100:1, 20:3, 10:1}, resultado)

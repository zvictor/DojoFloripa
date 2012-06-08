import random
import unittest2
from Palitos import Palitos

class TesteDosPalitos(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        print "TesteDosPalitos:"
        
    def setUp(self):
        pass

    def test_sem_operador(self):
        # testes devem sair sem operador
        um_palito = Palitos(1)
        self.assertEqual(um_palito.sem_operador(), "|")
        
        dois_palitos = Palitos(2)
        self.assertEqual(dois_palitos.sem_operador(), "||")
        
        tres_palitos = Palitos(3)
        self.assertEqual(tres_palitos.sem_operador(), "|||")
        
        zero_palito = Palitos(0)
        self.assertEqual(zero_palito.sem_operador(), "")
        
        menos_um_palito = Palitos(-1)
        self.assertRaises(ValueError, menos_um_palito.sem_operador)
        
    def test_com_multiplicao(self):
        # teste devem sair com multiplicacao
        um_palito = Palitos(1)
        self.assertEqual(um_palito.multiplicacao(), "|X|")
        
        dois_palitos = Palitos(2)
        self.assertIn(dois_palitos.multiplicacao(), ["|X||","||X|"])
        
        tres_palitos = Palitos(3)
        self.assertIn(tres_palitos.multiplicacao(), ["|X|||","|||X|"])
        
        vinte_palitos = Palitos(20)
        self.assertIn(vinte_palitos.multiplicacao(), ["||||X|||||","|||||X||||"])
        
        vinte_palitos = Palitos(100)
        self.assertIn(vinte_palitos.multiplicacao(), ["||||||||||X||||||||||"])
        
        vinte_palitos = Palitos(120)
        self.assertIn(vinte_palitos.multiplicacao(), ["||||||||||X||||||||||||", "||||||||||||X||||||||||"])
        
        zero_palito = Palitos(0)
        self.assertEqual(zero_palito.multiplicacao(), "X")
        
        menos_um_palito = Palitos(-1)
        self.assertRaises(ValueError, menos_um_palito.multiplicacao)
        
        
    def test_melhor_resultado(self):
        # teste devem sair com multiplicacao
        um_palito = Palitos(1)
        self.assertEqual(um_palito.melhor_resultado(), "|")
        
        dois_palitos = Palitos(2)
        self.assertIn(dois_palitos.melhor_resultado(), ["||"])
        
        tres_palitos = Palitos(3)
        self.assertIn(tres_palitos.melhor_resultado(), ["|||"])
        
        oito_palitos = Palitos(8)
        self.assertIn(oito_palitos.melhor_resultado(), ["||||||||", "||X||||", "||||X||"])
        
        nove_palitos = Palitos(9)
        self.assertIn(nove_palitos.melhor_resultado(), ["|||X|||"])
        
        nove_palitos = Palitos(11)
        self.assertIn(nove_palitos.melhor_resultado(), ["|||||||||||"])
        
        vinte_palitos = Palitos(20)
        self.assertIn(vinte_palitos.melhor_resultado(), ["||||X|||||","|||||X||||"])
        
        vinte_palitos = Palitos(100)
        self.assertIn(vinte_palitos.melhor_resultado(), ["||||||||||X||||||||||"])
        
        vinte_palitos = Palitos(120)
        self.assertIn(vinte_palitos.melhor_resultado(), ["||||||||||X||||||||||||", "||||||||||||X||||||||||"])
        
        zero_palito = Palitos(0)
        self.assertEqual(zero_palito.melhor_resultado(), "")
        
        menos_um_palito = Palitos(-1)
        self.assertRaises(ValueError, menos_um_palito.melhor_resultado)
        


if __name__ == '__main__':
    unittest2.main()
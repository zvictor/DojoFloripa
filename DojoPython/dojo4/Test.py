import unittest2
from MiojoSolverInterativo import MiojoSolverIterativo

class MiojoSolverIterativoTest(unittest2.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "MiojoSolverIterativoIterativo:"
        
    def setUp(self):
        pass

    def test_753(self):
        miojo_solver = MiojoSolverIterativo(5, 7)
        tempo_minimo = miojo_solver.resolver_para(3)
        self.assertEqual(tempo_minimo, 10)

    def test_853(self):
        miojo_solver = MiojoSolverIterativo(8, 5)
        tempo_minimo = miojo_solver.resolver_para(3)
        self.assertEqual(tempo_minimo, 8)

    def test_754(self):
        miojo_solver = MiojoSolverIterativo(7, 5)
        tempo_minimo = miojo_solver.resolver_para(4)
        self.assertEqual(tempo_minimo, 14)

    def test_6103(self):
        miojo_solver = MiojoSolverIterativo(6, 10)
        tempo_minimo = miojo_solver.resolver_para(3)
        self.assertEqual(tempo_minimo, None)

    def test_1074(self):
        miojo_solver = MiojoSolverIterativo(10, 7)
        tempo_minimo = miojo_solver.resolver_para(4)
        self.assertEqual(tempo_minimo, 14)

    def test_1076(self):
        miojo_solver = MiojoSolverIterativo(10,7)
        tempo_minimo = miojo_solver.resolver_para(6)
        self.assertEqual(tempo_minimo, 20)

import unittest2
from MiojoSolver import MiojoSolver

class MiojoSolverTest(unittest2.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "MiojoSolverTest:"
        
    def setUp(self):
        pass

    def test_753(self):
        miojo_solver = MiojoSolver(5, 7)
        tempo_minimo = miojo_solver.resolver_para(3)
        self.assertEqual(tempo_minimo, 10)


class MiojoSolver:
    def __init__(self, ampulheta1, ampulheta2):
        self.ampulheta1 = ampulheta1
        self.ampulheta2 = ampulheta2

    def resolver_para(self, tempo_miojo):
        maior = max(self.ampulheta1, self.ampulheta2)
        menor = min(self.ampulheta1, self.ampulheta2)

        if (maior - menor) == tempo_miojo:
            return maior

        resto_menor = menor % tempo_miojo
        resto_maior = maior % tempo_miojo

        if resto_maior + resto_menor == tempo_miojo:
            if (resto_menor > resto_maior):
                return 2 * menor
            return 2*maior

        elif resto_menor == tempo_miojo / 2.0:
            return maior * 2
        elif resto_maior == tempo_miojo / 2.0:
            return menor * 2
        
        return None    

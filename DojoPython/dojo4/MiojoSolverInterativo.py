class MiojoSolverIterativo:
    def __init__(self, ampulheta1, ampulheta2):
        self.ampulheta1 = ampulheta1
        self.ampulheta2 = ampulheta2
        
    def resolve(self, tempo_miojo):
        return self.maior() - self.menor() == tempo_miojo

    def vira_ampulheta(self):
        if self.ampulheta1 < self.ampulheta2:    
           self.ampulheta1 = 2 * self.ampulheta1
           #self.ampulheta2 = self.maior() - self.menor()
        else:
            self.ampulheta2 = 2 * self.ampulheta2
            #self.ampulheta1 = self.maior() - self.menor()

    def resolver_para(self, tempo_miojo):
        while not self.resolve(tempo_miojo):
            self.vira_ampulheta()
        return max(self.ampulheta1, self.ampulheta2)


    def maior(self):
        return max(self.ampulheta1, self.ampulheta2)

    def menor(self):
        return min(self.ampulheta1, self.ampulheta2)

import math

class Palitos:
    
    def __init__(self, numero):
        self.numero = numero
        
        
    def sem_operador(self):
        if self.numero < 0:
            raise ValueError('Valor negativo nao valido!')
        representacao = ""
        for i in range(self.numero):
            representacao += "|"
            
        return representacao
    
    def multiplicacao2(self):
        if self.numero < 0:
            raise ValueError('Valor negativo nao valido!')
        
        if self.numero == 0:
            return "X"
        
        lista= []
        for i in range(1, self.numero+1):
            if((self.numero) % i == 0):
                lista.append((i+self.numero/i, i, self.numero / i))
        
        result = sorted(lista, key=lambda x: x[0])[0]
        
        return  Palitos(result[1]).sem_operador() + "X" + Palitos(result[2]).sem_operador()
    
    def multiplicacao(self):
        if self.numero < 0:
            raise ValueError('Valor negativo nao valido!')
        
        if self.numero == 0:
            return "X"
       
        sqrt = int(math.sqrt(self.numero))
        
        while(True):
            if (self.numero%sqrt == 0):
                return Palitos(sqrt).sem_operador() + "X" + Palitos(self.numero/sqrt).sem_operador()
            sqrt+=1
    
    def melhor_resultado(self):
        
        multiplicacao= self.multiplicacao()
        
        if len(multiplicacao)+1 < self.numero:
            return multiplicacao
        else:
            return self.sem_operador()
        

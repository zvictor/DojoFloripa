class CaixaEletronico:
	def __init__(self, notas_disponiveis = {100:1000, 50:1000, 20:1000, 10:1000}):
		self.notas_disponiveis = notas_disponiveis
	
	def saque(self, valor):
		resultado= {}
		resto = valor % 100
				
		for nota in sorted(self.notas_disponiveis.keys(),reverse=True):
			if nota > valor: continue
			if self.notas_disponiveis[nota] == 0: continue
			resultado[nota]= valor / nota
			valor = valor%nota
			self.notas_disponiveis[nota] -= resultado[nota]
		return resultado

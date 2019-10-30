import pdb 

class Notas(): 
	
	def __init__(self, computador, computador1, computador2): 
		self.computador = computador 
		self.computador1 = computador1 
		self.computador2 = computador2 
		
		computadores_ligados = [1,2,3]

		pdb.set_trace() 
		if computador in computadores_ligados:
			print(f'Computador {computador} está ligado!')
		elif computador1 in computadores_ligados:
			print(f'Computador {computador1} está ligado!')
		elif computador2 in computadores_ligados:
			print(f'Computador {computador2} está ligado!')
		else:
			print('Nenhum computador está ligado!')
		

notas = Notas(5, 3, 4)
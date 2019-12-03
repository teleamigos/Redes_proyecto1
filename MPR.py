import time

class MPR():
	def __init__(self):
		self.vecinos = {'1':['0','2','3'],'2':['0','1','3']} #Para nodo 0
		#self.vecinos = {'0':['1','2'],'2':['0','1','3'], '3':['1','2','4']} #Para nodo 1
		#self.vecinos = {'0':['1','2'],'1':['0','2','3'],'3':['1','2','4']} #Para nodo 2
		#self.vecinos = {'1':['0','2','3'],'2':['0','1','3'],'4':['3','5']} #Para nodo 3
		#self.vecinos = {'3':['1','2','4'], '5':['4']} #Para nodo 4
		#self.vecinos = {'4':['3','5']} #Para nodo 5
		self.id = '0'
		self.nei = []
		self.around = []
		self.MPR = []

	def k_MPR(self):
		for i in self.vecinos:
			self.nei.append(i)
			for j in self.vecinos[i]:
				try:
					self.around.index(j)
				except:
					self.around.append(j)
		self.around.sort()
		self.around.remove(self.id)
		for i in self.nei:
			try:
				self.around.remove(i)
			except:
				time.sleep(0.05)

		#print(self.nei)
		#print(self.around)

		aux = 0
		for k in self.around:
			for i in self.vecinos:
				for j in self.vecinos[i]:
					if k == j and aux == 0:
						try:
							self.MPR.index(i)
						except:
							self.MPR.append(i)
							aux = 1
			aux = 0
		print("Los MPR's del nodo " + self.id + " son:")
		print(self.MPR)

MPR = MPR()
MPR.k_MPR()

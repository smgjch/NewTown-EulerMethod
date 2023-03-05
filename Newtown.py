from math import cos,sin
# ~ from sympy import sym
class FunctionToN():
	def __init__(self):
		self.x = 1.1
		self.fx =  -285 + 41/self.x + 74/self.x**2 + 123/self.x**3+ 90/self.x**4+ 55/self.x**5+ 20/self.x**6- 31/self.x**6
		self.f_x = 0
		
		# ~ self.function =
		# ~ self.defferential_function = 3 + sin(self.x)
		self.guess = 1.1
		self.accurace = 0.0000000000001
		
	def calc_fx(self):
		self.fx =  -285 + 41/self.x + 74/self.x**2 + 123/self.x**3+ 90/self.x**4+ 55/self.x**5+ 20/self.x**6- 31/self.x**6
	
	def calc_f_x(self):
		self.f_x = -41/self.x**2 - 2*74/self.x**3 - 3*123/self.x**4 - 4*90/self.x**5 - 5*55/self.x**6+ 6*20/self.x**7 + 6*31/self.x**7
	
	
	def newton_method(self):
		self.x = self.guess
		self.calc_fx()
		self.calc_f_x()
		self.guess = self.x - self.fx/self.f_x
		
	def run(self):
		while True:
			if self.fx < self.accurace and self.fx > -1*self.accurace:
				return self.x
			else:
				self.newton_method()
				

test = FunctionToN()
print(test.run())


class FunctionToNewN:
	def __init__(self):
		self.x = sym.Symbol("x")
		self.y = sym.Symbol("y")
		self.dy = sym.Symbol("dy")
		
		self.y = -2*self.x**3+self.x**2-2*self.x+1
		
		# ~ self.function =
		# ~ self.defferential_function = 3 + sin(self.x)
		# ~ self.guess = 0
		self.accurace = 0.001
		
	def calc_y():
		self.y = -2*self.x**3+self.x**2-2*self.x+1	
		
	def newton_method(self):
		while True:
			pass
			
		
		
		
		
		
		

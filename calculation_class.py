class Calculation:
	def __init__(self,x,y):
		self.x = x	
		self.y = y

	def add(self):
		result = self.x + self.y
		return result

	def sub(self):
		result = self.x - self.y
		return result

	def mul(self):
		result = self.x * self.y
		return result	

	def div(self):
		result = self.x / self.y
		return result


a = Calculation(2,3)
a_1 = a.add()
print(a_1)

a_2 = a.sub()
print(a_2)

a_3 = a.mul()
print(a_3)

a_4 = a.div()
print(a_4)

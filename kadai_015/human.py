class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# メソッドを定義
	def printinfo(self):
		print(self.name, self.age)

person = Human("山田太郎", 30)
person.printinfo()

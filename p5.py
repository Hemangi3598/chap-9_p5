 wapp to display id, marks, name, address of student  and salary of hod and teacher using subclass & superclass
class person:
	def __init__(self, id, name, address):
		self.id = id
		self.name = name
		self.address = address
	def show(self):
		print("id = ", self.id)
		print("name = ", self.name)
		print("address = ", self.address)
class teacher(person):
	def __init__(self, id, name, address, salary):
		super().__init__(id, name, address)
		self.salary = salary
	def show(self):
		super().show()
		print("salary = ", self.salary)
class hod(teacher):
	def __init__(self, id, name, address, salary, dept):
		super().__init__(id, name, address, salary)
		self.dept = dept
	def show(self):
		super().show()
		print("dept = ", self.dept)

t = teacher(34, "radha", "parel", 25000)
t.show()
h = hod(45, "asha", "thane", 50000, "maths")
h.show()

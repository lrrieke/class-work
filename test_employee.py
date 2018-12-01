import unittest

from employee import Employee 

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.first_employee = Employee('patrick', 'caddick', 85000)

	def test_increment_raise(self):
		self.first_employee.give_raise()
		self.assertEqual(self.first_employee.salary, 90000)

	def test_custom_raise(self):
		self.first_employee.give_raise(10000)
		self.assertEqual(self.first_employee.salary, 95000)

unittest.main()

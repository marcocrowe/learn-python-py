# Copyright (c) 2021 Mark Crowe <https://github.com/markcrowe-com>. All rights reserved.
 
class CalculatorCLI:
	def printMenu(self):
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("5. Quit")
	def divide(self):
		lhsOperand = float(input("Enter number 1: "))
		rhsOperand = float(input("Enter number 2: "))
		print("{} / {} = {}".format(lhsOperand, rhsOperand, lhsOperand / rhsOperand))
	def multiply(self):
		count =  int(input("How many number do you want to sum: "))
		product = 1.0
		for number in range(count):
			product *= float(input("Enter number {} of {}: ".format(number + 1, count)))
		print("Product = {}".format(product))
	def subtract(self):
		lhsOperand = float(input("Enter number 1: "))
		rhsOperand = float(input("Enter number 2: "))
		print("{} - {} = {}".format(lhsOperand, rhsOperand, lhsOperand - rhsOperand))
	def sum(self):
		count =  int(input("How many number do you want to sum: "))
		sum = 0.0
		for number in range(count):
			sum += float(input("Enter number {} of {}: ".format(number + 1, count)))
		print("Sum = {}".format(sum))
	def run(self):
		while True:
			self.printMenu()
			commandCode = input("Enter your choice: ")
			match commandCode:
				case '1':
					self.sum()
				case '2':
					self.subtract()
				case '3':
					self.multiply()
				case '4':
					self.divide()
				case '5':
					print("Quit")
					break


calculatorCLI = CalculatorCLI()

calculatorCLI.run()

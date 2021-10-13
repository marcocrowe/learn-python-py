# Copyright (c) 2021 Mark Crowe <https://github.com/markcrowe-com>. All rights reserved.

class CalculatorCLI:
	'''A Command Line Interface (CLI) Calculator'''
	def printMenu(self):
		''' Prints the menu '''
		print("1. Add")
		print("2. Subtract")
		print("3. Multiply")
		print("4. Divide")
		print("5. Quit")
	def divide(self):
		'''Divides a number from another number'''
		dividend = self.inputFloat("Enter Dividend number: ")
		divisor = self.inputFloat("Enter divisor number: ")
		if divisor == 0:
			print("Division by 0 is infinity")
		else:
			print("{} / {} = {}".format(dividend, divisor, dividend / divisor))
	def inputFloat(self, text="Enter Number"):
		'''Reads a float by reading and coverting a string from standard Input.'''
		'''If an invalid float format is entered the function will continue to try to get a valid float from standard Input'''
		'''If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise SystemExit. On *nix systems, readline is used if available.'''
		while True:
			try:   return float(input(text))
			except ValueError: print("Not a Float")
			except (KeyboardInterrupt, EOFError): raise SystemExit
	def inputInt(self, text="Enter Integer"):
		'''Reads a int by reading and coverting a string from standard Input.'''
		'''If an invalid int format is entered the function will continue to try to get a valid int from standard Input'''
		'''If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise SystemExit. On *nix systems, readline is used if available.'''
		while True:
			try:   return int(input(text))
			except ValueError: print("Not a Integer")
			except (KeyboardInterrupt, EOFError): raise SystemExit
	def multiply(self):
		'''Multiplies a series of numbers'''
		count = self.inputInt("How many number do you want to multiply: ")
		product = 1.0
		for number in range(count):
			product *= self.inputFloat("Enter multiplier number {} of {}: ".format(number + 1, count))
		print("Product = {}".format(product))
	def subtract(self):
		'''Subtracts a number from another number'''
		minuend = self.inputFloat("Enter Minuend number: ")
		subtrahend = self.inputFloat("Enter Subtrahend number: ")
		print("{} - {} = {}".format(minuend, subtrahend, minuend - subtrahend))
	def sum(self):
		'''Sums a series of numbers'''
		count = self.inputInt("How many number do you want to sum: ")
		sum = 0.0
		for number in range(count):
			sum += self.inputFloat("Enter number {} of {}: ".format(number + 1, count))
		print("Sum = {}".format(sum))
	def run(self):
		'''Runs the calculator'''
		while True:
			self.printMenu()
			commandCode = input("Enter your choice: ")
			match commandCode:
				case '1': self.sum()
				case '2': self.subtract()
				case '3': self.multiply()
				case '4': self.divide()
				case '5':
					print("Goodbye")
					break
				case _: print("Invalid Choice:", commandCode)

calculatorCLI = CalculatorCLI()

calculatorCLI.run()
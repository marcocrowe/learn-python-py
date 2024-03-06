"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Hello World
"""


class CalculatorCLI:
    """A Command Line Interface (CLI) Calculator"""

    def print_menu(self) -> None:
        """Prints the menu"""
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

    def divide(self):
        """Divides a number from another number"""
        dividend: float = self.get_float_input("Enter Dividend number: ")
        divisor: float = self.get_float_input("Enter divisor number: ")
        if divisor == 0:
            print("Division by 0 is not defined.")
        else:
            print("{} / {} = {}".format(dividend, divisor, dividend / divisor))

    @staticmethod
    def get_float_input(text: str = "Enter Number: ") -> float:
        """Reads a float by reading and converting a string from standard Input. If an invalid
        float format is entered the function will continue to try to get a valid float from
        standard Input If the user hits EOF (*nix: Ctrl-D , Windows: Ctrl-Z+Return), raise
        SystemExit. On *nix systems, readline is used if available.

        Args:
            text (str, optional): The prompt to display. Defaults to "Enter Number: ".

        Raises:
            SystemExit: If the user hits EOF (*nix: Ctrl-D , Windows: Ctrl-Z+Return)

        Returns:
            float: The float entered by the user
        """
        while True:
            try:
                return float(input(text))
            except ValueError:
                print("Not a Float")
            except (KeyboardInterrupt, EOFError) as exception:
                raise SystemExit from exception

    @staticmethod
    def get_int_input(text: str = "Enter Number: ") -> int:
        """Reads a int by reading and converting a string from standard Input. If an invalid
        int format is entered the function will continue to try to get a valid int from
        standard Input If the user hits EOF (*nix: Ctrl-D , Windows: Ctrl-Z+Return), raise
        SystemExit. On *nix systems, readline is used if available.

        Args:
            text (str, optional): The prompt to display. Defaults to "Enter Number: ".

        Raises:
            SystemExit: If the user hits EOF (*nix: Ctrl-D , Windows: Ctrl-Z+Return)

        Returns:
            int: The float entered by the user
        """
        while True:
            try:
                return int(input(text))
            except ValueError:
                print("Not a Integer")
            except (KeyboardInterrupt, EOFError) as exception:
                raise SystemExit from exception

    def multiply(self):
        """Multiplies a series of numbers"""
        count = self.get_int_input("How many number do you want to multiply: ")
        product = 1.0
        for number in range(count):
            product *= self.get_float_input(
                "Enter multiplier number {} of {}: ".format(number + 1, count)
            )
        print("Product = {}".format(product))

    def subtract(self):
        """Subtracts a number from another number"""
        minuend = self.get_float_input("Enter Minuend number: ")
        subtrahend = self.get_float_input("Enter Subtrahend number: ")
        print("{} - {} = {}".format(minuend, subtrahend, minuend - subtrahend))

    def sum(self):
        """Sums a series of numbers"""
        count = self.get_int_input("How many number do you want to sum: ")
        sum = 0.0
        for number in range(count):
            sum += self.get_float_input(
                "Enter number {} of {}: ".format(number + 1, count)
            )
        print("Sum = {}".format(sum))

    def run(self):
        """Runs the calculator"""
        while True:
            self.print_menu()
            command_code: str = input("Enter your choice: ")
            match command_code:
                case "1":
                    self.sum()
                case "2":
                    self.subtract()
                case "3":
                    self.multiply()
                case "4":
                    self.divide()
                case "5":
                    print("Goodbye")
                    break
                case _:
                    print("Invalid Choice:", command_code)


calculatorCLI = CalculatorCLI()

calculatorCLI.run()

"""
Input 5 numbers from the keyboard (use a loop). Check that each number is between 1 and 10(use an if statement).
If it is not between 1 and 10, print a message saying the number must be between 1 and 10.
Count the number of valid entries i.e. the ones that are between 1 and 10. (This must be done inside the loop).
At the end of the script, display the total number of valid entries e.g.  "The number of valid entries was: 4"
"""

INPUT_COUNT = 7


def main() -> None:
    """Main function"""
    valid_entries = 0
    for number in range(INPUT_COUNT):
        number_input = int(input(f"Enter number {number + 1}: "))
        if number_input >= 1 and number_input <= 10:
            valid_entries += 1
        else:
            print("The number must be between 1 and 10.")
    print(f"The number of valid entries was: {valid_entries}")


if __name__ == "__main__":
    main()

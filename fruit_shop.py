"""
Copyright Mark Crowe (c) 2024

Problem description: You are going to write a script to calculate net price and discount for 
purchasing apples, bananas and pears.The price of a tray of apples is €3.00, the price of a KG 
of bananas is €2.20, the price of a tray of pears is €4.80. You will ask the user how many 
apples, bananas and pears they would like. Discount of 5% is applied to the total order. 
Calculate the total price net of discount. 
Print a message in the following format: The price of 99 apples, 99 bananas and 99 pears is €99.99,
where €99.99 is the relevant price.
"""

APPLE_TRAY_PRICE = 3
BANANA_KG_PRICE = 2.20
PEARS_TRAY_PRICE = 4.80

DISCOUNT_RATE = 0.05

def calculate_and_display_price(apple_trays: int, banana_kgs: float, pears_trays: int) -> None:
    """
    Calculate the price of the fruit and display the price
    
    Parameters:
    apple_trays (int): The number of apple trays
    banana_kgs (float): The number of KGs of bananas
    pears_trays (int): The number of pear trays
    """
    price = apple_trays * APPLE_TRAY_PRICE + banana_kgs * BANANA_KG_PRICE + pears_trays * PEARS_TRAY_PRICE
    total =price - (price*DISCOUNT_RATE)
    print(f"The price of {apple_trays} apples, {banana_kgs} bananas and {pears_trays} pears is €{total:.2f}")


def main()->None:
    """The main function"""

    calculate_and_display_price(1, 2,1)
    calculate_and_display_price(0, 3, 2)
    calculate_and_display_price(2, 0, 3)

    apple_trays = int(input("How many trays of apples would you like?"))
    banana_kgs = float(input("How many KGs of bananas would you like?"))
    pears_trays = int(input("How many trays of pears would you like?"))

    calculate_and_display_price(apple_trays, banana_kgs, pears_trays)

if __name__ == "__main__":
    main()

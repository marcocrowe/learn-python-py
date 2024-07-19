"""
Write a short script to calculate pay from hours worked.
 
Ask the user to input their hours worked in a week from the keyboard.
 
Pay is calculated at a rate of €10 per hour for hours worked up to 40 hours. 
Overtime is paid at a rate of time and a half (1.5 times normal rate) 
for any hours worked above 40 hours.
 
Tax is calculated as 20% of pay.
 
Calculate the net pay
 
Display the result.
 
"""

STANDARD_PAY_RATE = 10
OVERTIME_MODIFIER = 1.5
OVERTIME_PAY_RATE = STANDARD_PAY_RATE *OVERTIME_MODIFIER
TAX_RATE = .2
STANDARD_PAY_HOURS=40

hours=50
gross_pay = 0

if hours > STANDARD_PAY_HOURS:
    gross_pay = STANDARD_PAY_HOURS * STANDARD_PAY_RATE
    overtime_hours= hours - STANDARD_PAY_HOURS
    overtime_pay = overtime_hours * OVERTIME_PAY_RATE 
    gross_pay += overtime_pay 
else:
    gross_pay = hours * STANDARD_PAY_RATE
tax = TAX_RATE * gross_pay
net_pay = gross_pay - tax
print(f"Total pay is {net_pay}")

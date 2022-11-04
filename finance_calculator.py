import math

# Users input it stored in a variable called user_choice
user_choice = input('''Choose either 'investment' or 'bond' from the menu below to proceed: \n 
investment\t-\tto calculate the amount of interest you will earn on your investment
bond\t\t-\tto calculate the amount you'll have to pay on a home loan\n''').lower()

# If user choice is equal to investment, get more information from the user specifically, deposit amount, interest rate,
# length of investment and whether the interest if simple or compound
if user_choice == "investment":
    deposit_amount = int(input("\nHow much is your deposit?: "))
    investment_interest_rate = int(input("What is the interest rate? (Only enter a number not the '%' symbol: "))
    years = int(input("How many years to you intend to invest?: "))
    interest = input("Would you like simple or compound interest? Simple/Compund: ").lower()

    # If the interest is simple, calculate and display the expected return
    if interest == "simple":
        total = deposit_amount * (1 + investment_interest_rate/100 * years)
        print(f"\nBased on your deposit of {deposit_amount} after {years} years, at {investment_interest_rate}% you will receive: {total}")

    # If the interest is compound, calculate and display the expected return
    elif interest == "compound":
        total = deposit_amount * math.pow((1 + investment_interest_rate/100), years)
        rounded_total = round(total,2)
        print(f"\nBased on your deposit of {deposit_amount} after {years} years, at {investment_interest_rate}% you will receive: {rounded_total}")

    # If user did not enter a valid option, display error message and end the program
    else:
        print("You have no selected a valid option. Please restart the program and try again.")

# If the user_choice entered was bond, get more information specifically, the current value of the property, the interest rate
# and, the length of time for repayment in months. Calculate the monthly repayments and display it to the user.
elif user_choice == "bond":
    present_value = float(input("What is the current value of the house?: "))
    bond_interest_rate = float(input("What is the interest rate? (Only enter a number not the '%' symbol: "))
    months = float(input("How many months do you plan to take to repay the bond?: "))
    monthly_interest = (bond_interest_rate/100) / 12
    repayment = (monthly_interest * present_value) / (1 - math.pow((1 + monthly_interest),(-months)))
    rounded_repayment = round(repayment, 2)

    print(f"\nYour monthly repayment amount will be: {rounded_repayment} per month.")

# If user did not enter a valid option, display error message and end the program
else:
    print("You have no selected a valid option. Please restart the program and try again.")

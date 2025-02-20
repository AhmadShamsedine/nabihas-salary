print("Hello Nabiha welcome to your monthly report ")

def get_amounts(salary):
    """
    Prompts the user to enter the amounts for savings, rent, and electricity, and calculates the total amount.
    """
    print("Nabiha, please enter the following amounts: ")
    
    while True:
        try:
            savings_amount = float(input("Savings ($): "))
            rent_amount = float(input("Rent ($): "))
            electricity_amount = float(input("Electricity ($): "))
            
            total_amount = savings_amount + rent_amount + electricity_amount
            remainder = salary - total_amount
            yearlyrent = rent_amount * 12
            yearlyelectricity = electricity_amount * 12
            totalsalaryrased2 = salary **2
            newsaving = savings_amount + 50

            print(f"Thank you, Nabiha! Your amounts are: Savings: ${savings_amount:.2f}, Rent: ${rent_amount:.2f}, Electricity: ${electricity_amount:.2f}.")
            print(f"The total amount spent is: ${total_amount:.2f}.")
            print(f"The remainder of your salary after expenses is: ${remainder:.2f}.")
            print(f"The yearly rent cost : ${yearlyrent:.2f}.")
            print(f"The yearly Electricity cost : ${yearlyelectricity:.2f}.")
            print(f"Total salary for the month raised to the power of 2 : ${totalsalaryrased2:.2f}.")
            print(f"The ammount of saving after adding 50 $ is : ${newsaving:.2f}.")
            break
            
        except ValueError:
            print("Invalid input. Please enter numeric values for the amounts.")
def get_salary():
    """
    Prompts the user to enter their monthly salary and returns the value.
    """
    while True:
        try:
            salary = float(input("Nabiha, please enter your salary for the month: "))
            print(f"Thank you, Nabiha! Your salary for the month is ${salary:.2f}.")
            return salary
        except ValueError:
            print("Invalid input. Please enter a numeric value for the salary.")

def get_month():
    """
    Prompts the user to enter a month and validates the input.
    """
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        user_input = input("Please enter the name of a month: ")
        if user_input.capitalize() in months:
            print(f"Welcome to {user_input.capitalize()}.")
            break
        else:
            print("Invalid month. Please enter a real month of the year.")
            
def main():
    """
    Main function that coordinates the flow of the program.
    """
    get_month()
    salary = get_salary()
    get_amounts(salary)

if __name__ == "__main__":
    main()                       
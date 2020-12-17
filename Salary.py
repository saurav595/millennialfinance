from verification import verify_numberinput
from verification import verify_age

class Salarycalc:

    def __init__(self, salary, age):
        self.salary = salary
        self.age = age

    def optimal_rent(self):
        '''
        Method: Calculates Optimal Rent that the user should pay
        Parameters: None
        Return: One float/int
        '''

        RENT_PERC = 0.2
        optimum_rent = self.salary * RENT_PERC
        return optimum_rent

    def buy_or_rent(self):
        '''
        Method: Calculates whether the user should buy or rent a living space
        Parameters: None
        Return: None (Just print statements)
        '''

        value_of_house = input("Enter the value of the house you want to purchase: $")
        while verify_numberinput(value_of_house) == False:
            print("Value of house is incorrect, it needs to be a number, please try again!")
            value_of_house = input("Enter the value of the house you want to purchase: $")

        rent_paid = input("Enter rent you're currently paying: $")
        while verify_numberinput(rent_paid) == False:
            print("Rent paid is incorrect, it needs to be a number, please try again!")
            rent_paid = input("Enter rent you're currently paying: $")

        value_of_house = float(value_of_house)
        rent_paid = float(rent_paid)

        FIVE_PERC_RULE = 0.05
        MONTHS_IN_YEAR = 12

        if (value_of_house*FIVE_PERC_RULE)/MONTHS_IN_YEAR > rent_paid:
            print("You're better off renting after considering the opportunity cost!")
        else:
            print("You should buy the house, it would be the better financial decision")

    def savings(self):
        '''
        Method: Calculates what the optimal savings should be based on age
        Parameters: None
        Return: 1 float (Just print statements with the savings)
        '''

        SAVINGS_ALLOCATION_V_AGE_DICT = {"18-29": 0.2, "30-39": 0.3, "40-49": 0.4, "50 - 100": 0.5}

        if 18 <= self.age <= 29:
            savings = self.salary * SAVINGS_ALLOCATION_V_AGE_DICT["18-29"]
        elif 30 <= self.age <= 39:
            savings = self.salary * SAVINGS_ALLOCATION_V_AGE_DICT["30-39"]
        elif 40 <= self.age <= 49:
            savings = self.salary * SAVINGS_ALLOCATION_V_AGE_DICT["40-49"]
        elif 50 <= self.age <= 100:
            savings = self.salary * SAVINGS_ALLOCATION_V_AGE_DICT["50-100"]
        return savings

    def retirement_age(self):
        '''
        Method: Calculates if the retirement age and target spend would make the user run out of money in the long run
        Parameters: None
        Return: None (Just print statements)
        '''

        target_age = input("Enter your planned retirement age: ")
        while verify_age(target_age) == False:
            print("Incorrect Age input, please try again!")
            target_age = input("Enter your planned retirement age: ")

        target_age = int(target_age)

        target_spend = input("Enter how much you would be spending every MONTH during your retirement: $")
        while verify_numberinput(target_spend) == False:
            print("Incorrect input on the spend, please enter digits and try again!")
            target_spend = input("Enter how much you would be spending every MONTH during your retirement: $")

        target_spend = float(target_spend)


        time_left = target_age - self.age
        current_savings = self.savings()

        GROWTH_RATE = 0.06
        TARGET_SPEND_RATE_IDEAL = 0.04

        savings_at_retirement = current_savings * time_left * ((1 + GROWTH_RATE)**time_left)

        if target_spend <= TARGET_SPEND_RATE_IDEAL * savings_at_retirement:
            print("With the current plan, you will be able to retire and never run out of money")
        else:
            print("You will not be able to survive on your current plan")


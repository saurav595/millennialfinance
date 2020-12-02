class Salarycalc:

    def __init__(self, salary, age):
        self.salary = salary
        self.age = age

    def optimal_rent(self):
        optimum_rent = self.salary * 0.2
        return optimum_rent

    def buy_or_rent(self):
        value_of_house = float(input("Enter the value of the house you want to purchase: "))
        rent_paid = float(input("Enter rent you're currently paying: "))

        if (value_of_house*0.05)/12 > rent_paid:
            print("You're better off renting after considering the opportunity cost!")
        else:
            print("You should buy the house, it would be the better financial decision")

    def savings(self):
        if 18 <= self.age <= 29:
            savings = self.salary * 0.2
        elif 30 <= self.age <= 39:
            savings = self.salary * 0.3
        elif 40 <= self.age <= 49:
            savings = self.salary * 0.4
        elif 49 <= self.age <= 100:
            savings = self.salary * 0.5
        return savings

    def retirement_age(self):

        target_age = int(input("Enter your planned retirement age: "))
        target_spend = float(input("Enter how much you would be spending every MONTH during your retirement: "))

        time_left = target_age - self.age
        current_savings = self.savings()

        savings_at_retirement = current_savings * time_left * (1.06**time_left)

        if target_spend <= 0.04*savings_at_retirement:
            print("With the current plan, you will be able to retire and never run out of money")
        else:
            print("You will not be able to survive on your current plan")


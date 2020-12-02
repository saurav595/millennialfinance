from Menu import menu #for the menu options
from Salary import Salarycalc #for the salary calculations like optimum rent, buy or rent, savings and retirement age
from credit_score import Credit_Score_Analysis #for the credit score computations like credit check and credit score analysis
from budget import budget #for creating the budget file
from ZipCode import zip_code #converts zip code to city, province
from adminfile import saveinput #function to save input on a txt file
from intro_message import intro #function to print the intro message

def main():
    #function that prints the intro message
    intro()

    #main inputs for the program
    name_input = input("Enter your name: ")
    email_input = input("Enter your email ID: ")
    salary_input = float(input("Enter your post-tax monthly salary: "))
    age_input = int(input("Enter your age: "))
    zipcode_input = input("Enter your zip code: ")

    #zip_code conversion to city,province
    city_province = zip_code(zipcode_input)
    city = city_province[0]
    province = city_province[1]

    credit_score = None

    #creating an object
    user_x = Salarycalc(salary_input, age_input)

    #prints menu
    user_input = menu()

    #loop to check the user input
    while user_input != 0:

        if user_input == 1:
            optimal_rent = user_x.optimal_rent()
            print("You should not be paying more than $" + str(round(optimal_rent)) + " per month as rent!")
        elif user_input == 2:
            user_x.buy_or_rent()
        elif user_input == 3:
            savings = user_x.savings()
            print("You should be saving at least $" + str(round(savings)) + " per month")
        elif user_input == 4:
            user_x.retirement_age()
        elif user_input == 5 or user_input == 6:
            if credit_score == None:
                credit_score = int(input("Enter your credit score (if you don't have it, you can get it from Experian): "))
                user_y = Credit_Score_Analysis(credit_score)
            if user_input == 5:
                print(user_y.credit_score_review())
            elif user_input == 6:
                length_credit_history = int(input("Since how many years have you had some form of credit(Enter 0 if no credit)?: "))
                payment_history = input("Have you ever had late payments? Enter Y or N: ")
                if payment_history.lower() == "y":
                    late_payments = True
                else:
                    late_payments = False
                current_utilization = int(input("Enter how much of your credit card limit is utilized? (Please ignore the % sign): "))
                recent_credit_requests = input("Have you requested credit in the past 6 months? Enter Y or N: ")
                print("")
                if recent_credit_requests.lower() == "y":
                    requests = True
                else:
                    requests = False
                user_y.credit_analysis(length_credit_history, current_utilization/100, late_payments, requests)
        elif user_input == 7:
            budget(salary_input) #ask user for a path
            print("Your file has been downloaded!")

        user_input = menu()

    print("Goodbye! Thanks for using Millenial Finance.")

    #saving user inputs to a file
    saveinput(name_input,email_input,salary_input,age_input,zipcode_input,city,province,credit_score)

main()
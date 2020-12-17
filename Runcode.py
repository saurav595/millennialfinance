from Menu import menu #for the menu options
from Salary import Salarycalc #for the salary calculations like optimum rent, buy or rent, savings and retirement age
from credit_score import Credit_Score_Analysis #for the credit score computations like credit check and credit score analysis
from budget import budget #for creating the budget file
from zipcode import zip_code #converts zip code to city, province
from adminfile import saveinput #function to save input on a txt file
from intro_message import intro #function to print the intro message
from verification import verify_email #function to verify email address is valid
from verification import verify_numberinput #function to verify salary is valid
from verification import verify_age #function to verify age is valid


def main():
    #function that prints the intro message
    intro()

    #main inputs for the program

    name_input = input("Enter your name: ")
    name_input_copy = name_input.replace(" ","")

    #defensive coding for name input
    while name_input_copy.isalpha() == False:
        print("Name can't have numbers or special characters in them, please retry")
        name_input = input("Enter your name: ")
        name_input_copy = name_input.replace(" ", "")

    #defensive coding for email input
    email_input = input("Enter your email ID: ")
    while verify_email(email_input) == False:
        print("Incorrect Email ID, please try again")
        email_input = input("Enter your email ID: ")

    #defensive coding for salary input
    salary_input = input("Enter your post-tax monthly salary: $")
    while verify_numberinput(salary_input) == False:
        print("Salary input should just be a number, please try again!")
        salary_input = input("Enter your post-tax monthly salary: $")

    #defensive coding for age_input
    age_input = input("Enter your age: ")
    while verify_age(age_input) ==  False:
        print("Age should just be a digit between 18-99")
        age_input = input("Enter your age: ")

    #defensive coding for zip code input
    zipcode_input = input("Enter your zip code: ")
    while zip_code(zipcode_input) == False:
        print("Zip code is incorrect, please try again!")
        zipcode_input = input("Enter your zip code: ")

    #zip_code conversion to city,province
    city_province = zip_code(zipcode_input)
    city = city_province[0]
    province = city_province[1]

    credit_score = None

    #creating an object on the Salary class
    user_x = Salarycalc(float(salary_input), int(age_input))

    #prints menu
    user_input = menu()

    #Dictionary to capture different options for ease of reader
    USER_INPUT_DICT = {"Option1": '1', "Option2": '2', "Option3": '3', "Option4":'4',
                       "Option5": '5', "Option6": '6', "Option7": '7', "OptionExit": '0'}

    #loop to check the user input
    while user_input != USER_INPUT_DICT["OptionExit"]:

        if user_input == USER_INPUT_DICT["Option1"]:
            optimal_rent = user_x.optimal_rent()
            print("You should not be paying more than $" + str(round(optimal_rent)) + " per month as rent!")
        elif user_input == USER_INPUT_DICT["Option2"]:
            user_x.buy_or_rent()
        elif user_input == USER_INPUT_DICT["Option3"]:
            savings = user_x.savings()
            print("You should be saving at least $" + str(round(savings)) + " per month")
        elif user_input == USER_INPUT_DICT["Option4"]:
            user_x.retirement_age()
        elif user_input == USER_INPUT_DICT["Option5"] or user_input == USER_INPUT_DICT["Option6"]:
            if credit_score == None:
                user_y = Credit_Score_Analysis()
            if user_input == USER_INPUT_DICT["Option5"]:
                print(user_y.credit_score_review())
            elif user_input == USER_INPUT_DICT["Option6"]:
                user_y.credit_analysis()
        elif user_input == USER_INPUT_DICT["Option7"]:
            budget(float(salary_input))
        else:
            print("Incorrect Input, please try again!")
        credit_score = user_y.get_credit_score()

        user_input = menu()

    print("Goodbye! Thanks for using Millenial Finance.")

    #saving user inputs to a file
    saveinput(name_input,email_input,salary_input,age_input,zipcode_input,city,province,credit_score)

main()
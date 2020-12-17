from verification import verify_credit_score
from verification import verify_age
from verification import verify_response
from verification import verify_utilization
from verification import verify_years

class Credit_Score_Analysis:

    def __init__(self):
        credit_score = input("Enter your credit score (if you don't have it, you can get it from Experian): ")
        while verify_credit_score(credit_score) == False:
            print("Incorrect Credit Score, it should be a 3 digit number between 300 and 850!")
            credit_score = input("Enter your credit score (if you don't have it, you can get it from Experian): ")
        self.credit_score = int(credit_score)

    def credit_analysis(self):
        '''
        Method: Analyzes the credit score that the user has
        Parameters: None
        Return: none (Just print statements)
        '''

        IDEAL_LENGTH_CREDIT_HISTORY_YEARS = 3
        UNTIMELY_PAYMENTS = True
        MAX_IDEAL_UTILIZATION_LEVEL = 0.32
        RECENT_REQUESTS_CREDIT = True

        length_credit_history = input("Since how many years have you had some form of credit(Enter 0 if no credit)?: ")
        while verify_years(length_credit_history) == False:
            print("Incorrect years mentioned please try again!")
            length_credit_history = input("Since how many years have you had some form of credit(Enter 0 if no credit)?: ")
        length_credit_history = int(length_credit_history)

        payment_history = input("Have you ever had late payments?: ")
        while verify_response(payment_history) == False:
            print("Incorrect input, please try again")
            payment_history = input("Have you ever had late payments?: ")
        if payment_history.lower() == "y" or payment_history.lower() == "yes":
            late_payments = True
        else:
            late_payments = False

        current_utilization = input("Enter how much of your credit card limit is utilized? (Please ignore the % sign): ")
        while verify_utilization(current_utilization) == False:
            print("Incorrect input, please try again (remember to not enter the % sign)")
            current_utilization = input("Enter how much of your credit card limit is utilized? (Please ignore the % sign): ")
        current_utilization = int(current_utilization)/100

        recent_credit_requests = input("Have you requested credit in the past 6 months?: ")
        while verify_response(recent_credit_requests) == False:
            print("Incorrect input, please try again")
            recent_credit_requests = input("Have you requested credit in the past 6 months?: ")
        if recent_credit_requests.lower() == "y" or recent_credit_requests.lower() == "yes":
            requests = True
        else:
            requests = False

        if length_credit_history <= IDEAL_LENGTH_CREDIT_HISTORY_YEARS:
            print("Once you have a credit card for longer, your credit score would get better")
        if late_payments == UNTIMELY_PAYMENTS:
            print("Your credit score is suffering because of your late payments")
        if current_utilization >= MAX_IDEAL_UTILIZATION_LEVEL:
            print("Ideal utilization should be less than 30% at any point")
        if requests == RECENT_REQUESTS_CREDIT:
            print("Your credit score might be affected because of recent requests")
        if (length_credit_history > IDEAL_LENGTH_CREDIT_HISTORY_YEARS) and (late_payments == (not UNTIMELY_PAYMENTS)) \
                and (current_utilization <= MAX_IDEAL_UTILIZATION_LEVEL) and (requests == (not RECENT_REQUESTS_CREDIT)):
            print("Your credit should be good based on the inputs you have given :)")

    def credit_score_review(self):
        '''
        Method: To verify how good the credit score is
        Parameters: None
        Return: None (Print Statements)
        '''

        CREDIT_SCORE_REVIEW_DICT = {"800-850": "Exceptional Credit Score",
                                    "740-799": "Very good credit history!",
                                    "670-739": "Good score, but there's room for improvement!",
                                    "580-669": "Fair, you can improve it by using our credit score analysis tool",
                                    "300-579": "Poor Score, you will really struggle for optimal credit. Improve it using our credit analysis tool!"}
        if  800 <= self.credit_score <= 850:
            review = CREDIT_SCORE_REVIEW_DICT["800-850"]
        elif 740 <= self.credit_score <= 799:
            review = CREDIT_SCORE_REVIEW_DICT["740-799"]
        elif 670 <= self.credit_score <= 739:
            review = CREDIT_SCORE_REVIEW_DICT["670-739"]
        elif 580 <= self.credit_score <= 669:
            review = CREDIT_SCORE_REVIEW_DICT["580-669"]
        else:
            review = CREDIT_SCORE_REVIEW_DICT["300-579"]

        return review

    def get_credit_score(self):
        return self.credit_score
class Credit_Score_Analysis:

    def __init__(self, credit_score):
        self.credit_score = credit_score

    def credit_analysis(self, length_credit_history, current_utilization, payment_history,
                              recent_requests_credit):

        if length_credit_history < 3:
            print("Once you have a credit card for longer, your credit score would get better")
        if payment_history == True:
            print("Your credit score is suffering because of your late payments")
        if current_utilization >= 0.32:
            print("Ideal utilization should be less than 30% at any point")
        if recent_requests_credit == True:
            print("Your credit score might be affected because of recent requests")
        if length_credit_history > 3 and payment_history == False and current_utilization <= 0.32 and recent_requests_credit == False:
            print("Your credit should be good based on the inputs you have given :)")

    def credit_score_review(self):

        if  800 <= self.credit_score <= 850:
            review = "Exceptional Credit Score!"
        elif 740 <= self.credit_score <= 799:
            review = "Very good credit history!"
        elif 670 <= self.credit_score <= 739:
            review = "Good score, but there's room for improvement!"
        elif 580 <= self.credit_score <= 669:
            review = "Fair, you can improve it by using our credit score analysis tool"
        elif 300 <= self.credit_score <= 579:
            review ="Poor Score, you will really struggle for optimal credit. Improve it using our credit analysis tool!"
        else:
            raise ValueError("Score should be in range of 300 - 850!")
        return review



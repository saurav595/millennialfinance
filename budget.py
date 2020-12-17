import xlsxwriter
from datetime import date

def budget(salary):
    ''' Function: To take in salary of the user and output a personalized
                budget plan for the user and also a tab to track expenses
        Parameters: Salary
        Return: 1 Excel
    '''
    #Generates today's date
    today = date.today()
    #Creates an excel in the same folder as source folder
    budget_plan = xlsxwriter.Workbook("Budget-Plan.xlsx")
    #Creates worksheet in the budget_plan workbook
    budget = budget_plan.add_worksheet("Budget")
    expenses = budget_plan.add_worksheet("Expenses")
    #sets column width
    budget.set_column(0,3,20)
    #adds the different formats we would want to use
    bold = budget_plan.add_format({'bold': True})
    money_format = budget_plan.add_format({'num_format': '$#,##0'})
    perc_format = budget_plan.add_format({"num_format": "0%" })

    #creates a skeleton of expenses worksheet

    expenses.write("B1","Expenses",bold)
    expenses.write("A2","Date",bold)
    expenses.write("B2","Category",bold)
    expenses.write("C2", "Amount", bold)

    expenses.set_column(0, 3, 20)

    expenses.data_validation("B3:B10000", {"validate":"list",
                                           "source":["Entertainment","Rent","Savings","Food","Health"],
                                           "input_title":"Select one of these options"})

    expenses.data_validation("A3:A10000", {"validate":"date",
                                           "criteria":"between",
                                           "minimum":date(2000,1,1),
                                           "maximum":date(2100,1,1),
                                           "input_title":"Enter a date",
                                           "error_title":"Only dates allowed here",
                                           "error_message":"Please enter a date in mm-dd-yyyy format"})

    expenses.data_validation("C3:C10000", {"validate":"decimal",
                                           "criteria":">",
                                           "minimum":0.1,
                                           "input_title":"Enter the spending here",
                                           "error_title":"Only numbers allowed here",
                                           "error_message":"Numbers greater than 0 allowed here"})

    #creates a skeleton of budget worksgeet
    budget.write("A1","Budget",bold)
    budget.write("B1","Date of Budget: " + today.strftime("%B %d, %Y"),bold)
    budget.write("A2","Line Item",bold)
    budget.write("B2","Allocation Percentage",bold)
    budget.write("C2","Maximum Spending",bold)


    #creates a list of the plan
    plan = [["Rent", 0.2, salary*0.2],
            ["Food", 0.1, salary*0.1],
            ["Savings",0.4,salary*0.4],
            ["Entertainment",0.1, salary*0.1],
            ["Health",0.2,salary*0.2]]

    row = 2
    column = 0

    #loop to allocate the plan to the worksheet

    for line_item, perc_allocation, max_spending in (plan):
        budget.write_string(row,column, line_item)
        budget.write_number(row, column + 1, perc_allocation,perc_format)
        budget.write_number(row, column + 2, max_spending,money_format)
        row += 1
    budget.write("A8","Total",bold)
    budget.write("B8","=sum(B3:B7)",perc_format)
    budget.write("C8","=sum(C3:C7)",money_format)

    budget_plan.close()
    print("Your file has been downloaded!")
    return budget_plan
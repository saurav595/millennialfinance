import re

def verify_email(email):
    '''
    Function: To verify whether email is valid
    Parameter: One string
    Return: One String or One boolean
    Inspired from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    '''

    check_1 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    check_2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if re.search(check_1,email):
        email = email
    elif re.search(check_2,email):
        email = email
    else:
        email = False
    return email

def verify_numberinput(number):
    '''
    Function: To verify if the string inputted is a valid number
    Parameter: 1 string
    Return: String if valid, or else a False (Boolean)
    '''

    check_1 = '^[0-9.]*$'

    if re.search(check_1, number):
        number = number
    else:
        number = False
    return number

def verify_age(age_input):
    '''
        Function: To verify if the string inputted is a valid age
        Parameter: 1 string
        Return: String if valid, or else a False (Boolean)
    '''

    check_1 = '^([1][8-9]|[2-9][0-9])$'

    if re.search(check_1,age_input):
        age_input = age_input
    else:
        age_input = False
    return age_input


def verify_credit_score(credit_score):
    '''
        Function: To verify if the string inputted is a valid 3 digit number
        Parameter: 1 string
        Return: String if valid, or else a False (Boolean)
    '''

    check_1 = '[3-7][0-9][0-9]|[8][0-4][0-9]|[8][5][0]$'

    if re.search(check_1, credit_score):
        credit_score = credit_score
    else:
        credit_score = False
    return credit_score

def verify_response(str):
    '''
    Function: To verify if the string inputtes is a valid yes/no response
    Parameter: 1 string
    Return: String if valid or else False(Boolean)
    '''

    check_1 = ["y","Yes","No","n","YES","NO","Y","N","yes","no"]

    if str in check_1:
        str = str
    else:
        str = False
    return str

def verify_utilization(str):
    '''
    Function: To verify if the string entered is a valid 2 digit number
    Parameter: 1 string
    Return: String if valid or else False (Boolean)
    '''

    check_1 = "^([0-9]|[1-9][0-9]|[1][0][0])$"

    if re.search(check_1,str):
        str = str
    else:
        str = False
    return str

def verify_years(str):
    '''
    Function: To verify if the string entered are number of years/fractional years
    Parameters: 1 str
    Return: Str or Boolean
    '''

    check_1 = "^([0-9]|[0-9][0-9])$"

    if re.search(check_1,str):
        str = str
    else:
        str = False
    return str
#intro to the program
def intro():
    '''
    Function: To create a pattern to display at start of code
    Parameters: None
    Return: None
    '''

    pat = '-$-'

    for i in range(1, 11, 2):
        string = pat * i
        print(string.center(43, '-'))

    print("Welcome to Millenial Finance".center(43, "-"))

    for i in range(11 - 2, -1, -2):
        string = pat * i
        print(string.center(43, '-'))
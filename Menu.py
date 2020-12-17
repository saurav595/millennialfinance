def menu():
    '''
    Function - To print menu options
    Parameters - None
    Return - Inputted option
    '''

    print("\n" + "MENU".center(43,"-") + "\n \
        1 - Rent Calculator \n \
        2 - Rent vs. Buy \n \
        3 - How much should I save? \n \
        4 - Will I be able to retire on time? \n \
        5 - Credit Score Check \n \
        6 - Credit Score Analysis \n \
        7 - Generate personal budget \n \
        0 - Quit \n")

    selected_option = input("Select your option: ")

    return selected_option


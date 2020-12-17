import datetime

def saveinput(name, email, salary, age, zipcode, city, province, credit_score):
    '''
    Function: To save a file with user inputs
    Parameter: 5 strings (name,email,zipcode,city,province);1 float(salary), 2 integers(age,credit_score)
    Return: File saved
    '''

    file = open("Saved Inputs","a")
    time = datetime.datetime.now()
    file.write(str(time)+"," + name + "," + email + "," + str(salary) +","+str(age)+","+str(zipcode)+","+ \
               str(city)+","+str(province)+","+str(credit_score)+"\n")
    file.close()




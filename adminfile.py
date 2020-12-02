import datetime

def saveinput(name, email, salary, age, zipcode, city, province, credit_score):

    file = open("Saved Inputs","a")
    time = datetime.datetime.now()
    file.write(str(time)+"," + name + "," + email + "," + str(salary) +","+str(age)+","+str(zipcode)+","+ \
               str(city)+","+str(province)+","+str(credit_score)+"\n")
    file.close()




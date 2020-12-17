import csv

def zip_code(zip):
    '''
    Function: zip_code to input zip codes, search through the zip code file and return the city, state
    Parameters: 1 alphanumeric
    Return: City, State (Tuple) or False(Boolean)
    '''

    Allzipcodes = open("CanadianPostalCodes.csv","r")
    content = csv.reader(Allzipcodes, delimiter = ',')

    c_zip_code = ""

    if len(zip) == 6:
        c_zip_code = zip[0:3] + " " + zip[3:]
    else:
        c_zip_code = zip

    for row in content:
        if c_zip_code.upper() == row[0].upper():
            city = row[1],row[2]
            return city
        else:
            city = False
    Allzipcodes.close()
    return city
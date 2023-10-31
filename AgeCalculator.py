# Assignment1

def Agecalculator():
    year = int(input("Enter year of birth"))
    if year == 0:
        print("Zero is not an accepted input")
    
    elif year>1800 and year<2023:
        age = 2023 - year
        print("Age is: " + str(age))
    
    else:
        print("year is ou of bounds. Thank you for participating")


Agecalculator()

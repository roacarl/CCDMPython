
class OddEvenException(Exception):

    try:
        userchoice = int(input("Enter number"))
        if userchoice % 2 == 0:
           print(str(userchoice) + " is an even number")

        else:
            print(str(userchoice) + " is an Odd number")


    except OddEvenException:
        print("Sorry!!! Not a valid integer")




   
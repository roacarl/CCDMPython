# create a distance converter function
#Convert 500m to km
def distconverter(Meters):
    dist = Meters / 1000
    print(dist)

# To add more on Ansers

    print("distance is: " + str(dist) + "km")

# Call the function

distconverter(500)



def distconverter():
    choice = int(input("Enter 1 for m to km: \n enter 2 for km to m:"))

    if choice==1:
        dist = int(input("Enter distance in meter: "))
        ans= dist / 1000
        print("distance is: " + str(ans) + "km")

    elif choice==2:
        dist2 = int(input("Enter the distance in km: "))
        ans2 = dist2 * 1000
        print("distance is: " + str(ans2) + "meters") 

    else:
        print("sorry, wrong choice. Please select 1 or 2")

# Call the function
#distconverter()

        


#Exercise 1
#Write a program to create a function that takes two arguments, name and age, and print their value.
def nameage (name, age):
    print("Hi "+ name)
    print("Your age is:" + str(age))
    
#Call the function
nameage("Carl", 22)

#Exercise 2: Return multiple values from a function
#Write a program to create function calculation() such that it can accept two variables and calculate
#addition and subtraction.

def calculation (a , b):
    ans = a+b
    print(ans)

result=(calculation(10,15))




 




#Create a fuction name as GREETING

'''def greeting(Uname): # Uname is 
    p1 = "John"      # p1 is the local variable
    print("Hello There")

p2 = "Alex"  # p2 is global variable

print()
print(p2)
'''




# Class ---Cat

class cat:
    
    cat = "feline"
    #constructor
    def __init__(self,cname,color,weight,breed):
        self.cname = cname
        self.color = color
        self.weight = weight
        self.breed = breed

    #New function: just to print cats details

    def printCatDetails(self):
        print(".........Cat's details.......")
        print("Name: ", self.cname)
        print("Color: ", self.color)
        print("weight: ", self.weight, "in kg")
        print("Breed: ", self.breed)

userCname =str(input("Hi, please answer the following questions: \nCat's name: "))
usercolor = str(input("Cat's color? "))
userweith = str(input("cat's weight in kg? "))
userbreed = str(input("Cat's breed?"))



#Create  the Object
mycat = cat(userCname,usercolor,userweight,userbreed)

#use Object
mycat.printCatDetails()



        


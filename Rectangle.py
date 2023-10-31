

try:

    #create class Rectangle

    class Rectangle:

    #create constructor
        def __init__(self,length,width):
          self.length = length
          self.width = width

        def RectArea(self):
            print("Area is: ",self.length * self.width, " cm2")

        def RectPeri(self):
            print("Perimeter is: ",(2*self.length + 2*self.width), " cm")

    

    userlength = int(input("Enter length (cm): "))
    userwidth = int(input("Enter width (cm): "))

    #object instantiation . Attach to class only with parameters
    rectObj = Rectangle(userlength,userwidth)


    #use the object created. Call function here
    #rectObj.RectArea()
    #rectObj.RectPeri() 
    rectObj.myfuction()

    
except SyntaxError:
    print("Please check for missing colon or possible syntax error")

except AttributeError:
    print("Method not found. Use other method")

class Triangle:
    #constructor
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def triArea(self):
        print("Area is",self.base*self.height/2, "cm2")

TriBase=int (input("Enter your base (cm)"))
TriHeight=int(input("Enter your height (cm)"))

triObject=Triangle(TriBase,Triangle)

triObject.TriArea()

class perimiter:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def Triperi(self):
        print("Perimeter is",self.side1+self.side2+self.side3, "cm")

Ts1=int(input("Enter value of side1 (cm)"))
Ts2=int(input("Enter value of side2 (cm)"))
Ts3=int(input("Enter value of side3 (cm)"))
 
triObject=perimiter(Ts1,Ts2,Ts3)

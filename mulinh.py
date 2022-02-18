class Car():
    def Benz(self):
        print(" This is a Benz Car ")
class Bus():
    def Volvo(self):
        print(" This is a Volvo Bus ")
class Truck():
    def Eicher(self):
        print(" This is a Eicher Truck ")
class Plane():
    def Indigo(self):
        print(" This is a Indigo plane ")
class Transport(Car,Bus,Truck,Plane):
    def Main(self):
        print("This is the Main Class")
B=Transport()
B.Benz()
B.Volvo()
B.Eicher()
B.Indigo()
B.Main()
class customer:

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #method
    def purchase(self):
        return "{} has made a purchase".format(self.name)

Aakash = customer("Aakash", 21)
Eeshan = customer("Eeshan", 20)

# access the instance attributes
print(Aakash.purchase())
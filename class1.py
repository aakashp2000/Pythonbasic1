class customer:

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

Aakash = customer("Aakash", 21)
Eeshan = customer("Eeshan", 20)

# access the instance attributes
print("{} is {} years old".format( Aakash.name, Aakash.age))
print("{} is {} years old".format( Eeshan.name, Eeshan.age))
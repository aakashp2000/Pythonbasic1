# parent class
class Processor:

    def __init__(self):
        print("Processor is available for sale")

    def whoisThis(self):
        print("Processor")
# child class
class ryzen5(Processor):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Ryzen 5 is in stock")

    def whoisThis(self):
        print("Ryzen 5")

query = ryzen5()
query.whoisThis()

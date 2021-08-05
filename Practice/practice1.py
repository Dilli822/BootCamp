class mobile:
    name = "sony x5 dual"
    
    def __init__(self, color, ram):
        self.color = color
        self.ram = ram
    

    @classmethod
    def printMobile(cls):
        print("I have:",cls.name)

    @staticmethod
    def static(price):
        print("The price of this mobile is", price)

mobile.static(35000)
# this is class method calling
mobile.printMobile()

my_mobile = mobile("black", "3gb")
print(my_mobile.color)


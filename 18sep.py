class Book:

    def __init__(self):
        self.name = "Doms"
        self.cost = 60
        self.color = "red"  

    def help(self):
        print("os is reading")


b1 = Book()
print(b1.name)
print(b1.cost)
b1.help()
print(b1.color) 
b1.nop = 200
print(b1.nop)
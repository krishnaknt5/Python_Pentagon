class Laptop:
    def __init__(self):
        self.color="Black"
        self.model="V15"
        self.brand="Asus"
    def run(self):
        print("Laptop is running")
        print(self)
l1=Laptop()
print(l1.color)
print(l1.model)
print(l1.brand)
l1.run()
print(l1)       
l1.proc="I5"
print(l1.proc)


l1.model="V16"
print(l1.model)
# del l1.model
# print(l1.model)
l2=Laptop()
l2.model="V17"
print(l2.model)

l3=Laptop()
l3.model="V18"
print(l3.model)


del l1.model
print(l1.model)


del l2.model
print(l2.model)


del l3.model
print(l3.model)


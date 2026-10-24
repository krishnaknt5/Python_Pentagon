class Student:
    def __init__(self):
        self.name="Hari"
        self.age=36
        self.usn=420
        self.address="Russian"
    def study(self):
        print("Hari is studying")
s1=Student()
print(s1.name)
print(s1.age)
print(s1.address)
s1.study()
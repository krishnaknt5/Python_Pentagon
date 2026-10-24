class fan:
    def __init__(self):
        self.brand="Usha"
        self.cost=1500
        self.color="black"
    def on(self):
        print("Fan is on")
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")
f1=fan() #creation of obj
print(f1.brand)
print(f1.cost)
print(f1.color)
f1.on()
f1.rotate()
f1.off()
class Heroin:
    def __init__(self):
        self.name="Ruku"
        self.age=29
    def act(self):
            print("Rukku is a good actress")
h1=Heroin()
print(h1.name)
print(h1.age)        
h1.act()


h1.movie="Toxic"
print(h1.movie)

h1.age=30
print(h1.age)

del h1.movie
print(h1.movie)
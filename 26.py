class calci: 
    def __init__(self): 
        self.brand = "Casio" 
        self.color = "black" 
        
    def add(self): 
        a = 10 
        b = 20 
        c = a + b 
        return c 

C1 = calci() 
print(C1.brand) 
print(C1.color) 
res = C1.add()  
print(res)

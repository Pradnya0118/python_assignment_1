# garden class

class garden:
    #constructor/function

    def __init__(self,n,f,l):
        self.name=n
        self.flowers=f
        self.location=l

obj1=garden("rose",50,"pune")
obj2=garden("lily",30,"mumbai")

print(obj1.name)
print(obj1.flowers)
print(obj1.location)

print(obj2.name)
print(obj2.flowers)
print(obj2.location)


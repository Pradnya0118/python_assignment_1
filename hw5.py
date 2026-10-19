# Pizza Class

class pizza:

    def __init__(self,n,p,s):
        self.name=n
        self.price=p
        self.size=s

obj1=pizza("corn cheese",250,"medium")
obj2=pizza("margherita",199,"small")

print(obj1.name)
print(obj1.price)
print(obj1.size)

print(obj2.name)
print(obj2.price)
print(obj2.size)


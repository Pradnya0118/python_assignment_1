# Dance Class

class dance:
    #constructor/special method/function

    def __init__(self,n,d,l):
        self.name=n
        self.duration=d
        self.level=l

obj=dance("belly dance","1hr","beginner")

print(obj.name)
print(obj.duration)
print(obj.level)

obj.location="pune"
print(obj.location)

obj1=dance("hiphop","2hr","advanced")

print(obj1.name)
print(obj1.duration)
print(obj1.level)


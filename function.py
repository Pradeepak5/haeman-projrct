def addNum(a,b):
    c=a+b
    return c

def oddorEven(x):
    if(x%2==0):
        return "num 1 is even"
    else:
        return "num 1 is odd"

x=int(input("Enter num 1 : "))
y=int(input("Enter num 2 : "))

addition=addNum(x,y)
print(addition)

oddeven=oddorEven(x)
print(oddeven)




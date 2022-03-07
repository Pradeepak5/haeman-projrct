def divFun(x):
    if(x%8==0):
        return "divisible by 8"
    else:
        return"not divisible by 8"

a=int(input("Enter a number :"))
div=divFun(a)
print(div)
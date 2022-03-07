x=int(input("Enter the number :"))
y=int(input("Enter the number :"))
result=lambda a,b:a+b
print(result(x,y))

list1=[1,2,4,3,5,56,45,97,98,65,]
list2=list(filter(lambda x:(x%2==1),list1))
print(list2)
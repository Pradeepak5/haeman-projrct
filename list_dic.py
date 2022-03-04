book_list=[]
count=int(input("Enter the count :"))
for i in range(0,count):
    book_name=input("Enterr the book name :")
    Author_name=input("Enter book author name :")
    price=int(input("price of the book :"))
    publisher=input("Enter publisher name :")
    book_dic={"book name":book_name,"author name":Author_name,"price":price,"publisher":publisher}
    book_list.append(book_dic)

print(book_list)

for j in book_list:
    print(j['book name'])
    print(j["publisher"])

print(book_name)
a=[]
element=int(input("Enter the Number of Element::"))
for x in range(element):
    b=int(input("Enter The Element::"))
    a.append(b)
temp=a[0]
a[0]=a[element-1]
a[element-1]=temp
print("New List::",a)

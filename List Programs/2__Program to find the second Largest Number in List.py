a=[]
element=int(input("Enter The Number of Elements::"))
for i in range(element):
    b=int(input("Enter the Element::"))
    a.append(b)
a.sort()
print("The Second Largest Element of List::",a[element-2])

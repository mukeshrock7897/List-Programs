a=[]
element=int(input("Enter The Number of Elements::"))
for i in range(element):
    b=int(input("Enter the Element::"))
    a.append(b)
a.sort()
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("List Of Even::",even)
print("List Of Odd::",odd)



a=[]
element=int(input("Enter the Number of Element::"))
for x in range(element):
    b=int(input("Enter The Element::"))
    a.append(b)
c=set()
unique=[]
for x in a:
    if x not in c:
        unique.append(x)
        c.add(x)
print(unique)

a=[]
element=int(input("Enter the Number of Element::"))
for i in range(element):
    b=int(input("Enter The Element::"))
    a.append(b)
c=[sum(a[0:x+1]) for  x in range(0,len(a))]
print(c)

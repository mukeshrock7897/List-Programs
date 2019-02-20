a=[]
element1=int(input("Enter The Number of Elements For First List::"))
for i in range(element1):
    b=int(input("Enter the Element::"))
    a.append(b)
    
print("First List",a)
c=[]
element2=int(input("\n\nEnter The Number of Elements For Second List::"))
for i in range(element2):
    d=int(input("Enter the Element::"))
    c.append(d)
print("Second List::",c)
e=a+c
e.sort()
print("Merged And Sorted List::",e)


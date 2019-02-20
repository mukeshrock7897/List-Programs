a=[]
element=int(input("Enter the Number of Element::"))
for x in range(element):
    b=input("Enter The Element::")
    a.append(b)
max=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max):
        max=len(i)
        temp=max
print("Maximun Word Length ",temp)

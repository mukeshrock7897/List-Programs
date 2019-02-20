a=[]
element=int(input("Enter The Number Of Element For List::"))
for i in range(element):
    b=int(input("Enter The Element::"))
    a.append(b)
    
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("Second Largest Element of List::",a[element-2])

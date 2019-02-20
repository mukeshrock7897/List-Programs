a=[]
element=int(input("Enter the Number of Element::"))
for x in range(element):
    b=input("Enter The Element::")
    a.append(b)
print("Availble Element in List::",a)
c=[]
count=0
remove=input("Enter The Element To Remove::")
for i in a:
    if(i==remove):
        count=count+1
    else:
        c.append(i)
if(count==0):
    print("Item Not Found")
else:
    print("Number of Repetiton Element",count)
    print("Updated List::",c)

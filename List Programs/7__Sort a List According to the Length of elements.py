a=[]
element=int(input("Enter The Number Of Element For List::"))
for i in range(element):
    b=input("Enter The Element::")
    a.append(b)
a.sort(key=len)
print("Sorted Element According to Their Length::",a)

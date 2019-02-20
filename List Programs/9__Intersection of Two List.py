a=[]
element1=int(input("Enter The Number Of Element For 1st List::"))
for i in range(element1):
    b=input("Enter The Element::")
    a.append(b)
a.sort()
c=[]
element2=int(input("Enter The Number Of Element For 2nd List::"))
for i in range(element2):
    d=input("Enter The Element::")
    c.append(d)
c.sort()

def intersection(a,c):
    return list(set(a)&set(c))

print("Intersection of Two List",intersection(a,c))

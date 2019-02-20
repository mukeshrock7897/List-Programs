import random
a=[]
element=int(input("Enter the Number of Element::"))
for i in range(element):    
    a.append(random.randint(1,21))
print(a)

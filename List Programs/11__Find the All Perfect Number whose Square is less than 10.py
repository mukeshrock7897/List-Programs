lower=int(input("Enter the Lower Range Value::"))
upper=int(input("Enter The Upper Range Value::"))
a=[x for x in range(lower,upper+1) if(int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)

lower=int(input("Enter the Lower Range Value::"))
upper=int(input("Enter The Upper Range Value::"))
a=[(x,x**2) for x in range(lower,upper+1)]
print(a)

def last(n):
    return n[-1]
def sort(tuples):
    return sorted(tuples,key=last)
element=input("Enter the  Element::")
print(sort(element))

from functools import reduce

def Isprime(A):
    if A< 2:
        return False
    
    for i in range(2,A):
        if A% i == 0:
            return False
        
    return True


numbers = list(map(int, input("Enter numbers:").split()))

Filter= list(filter(Isprime,numbers))


Map= list(map(lambda x: x * 2,Filter))

Reduce= reduce(lambda a, b: a if a > b else b,Map)

print("List after filter =",Filter)
print("List after map =",Map)
print("List after reduce =",Reduce)

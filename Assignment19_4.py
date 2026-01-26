from functools import reduce


numbers = list(map(int, input("Enter numbers: ").split()))


Filter = list(filter(lambda x: x % 2 == 0, numbers))


Map= list(map(lambda x: x * x,Filter))


Reduce = reduce(lambda a, b: a + b,Map)

print("List after filter:",Filter)
print("List after map:",Map)

print("List after reduce:",Reduce)

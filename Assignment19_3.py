from functools import reduce


numbers = list(map(int, input("Enter numbers: ").split()))

Filter = list(filter(lambda x: x >= 70 and x <= 90, numbers))


Map= list(map(lambda x: x + 10, Filter))

Reduce = reduce(lambda x, y: x*y, Map)

print("List after filter:", Filter)
print("List after map:", Map)
print("List after reduce :",Reduce)

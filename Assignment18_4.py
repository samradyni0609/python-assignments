A=int(input("Enter number of elements:"))
list = []


for i in range(A):
    list.append(int(input()))

B= int(input("Enter element to search:"))
count = 0

for i in list:
    
    if i ==B:
        count = count + 1

print("frequency of number is", count)

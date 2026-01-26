A= int(input("Enter number of elements:"))

list = []


for i in range(A):
    list.append(int(input()))
    

min_num =list[0]

for i in list:
    if i<min_num:
        min_num =i

print("Minimum number is:",min_num)

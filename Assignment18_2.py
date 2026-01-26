A= int(input("Enter number of elements:"))

list = []


for i in range(A):
    list.append(int(input()))
    

max_num =list[0]

for i in list:
    if i> max_num:
        max_num =i

print("Maximum number is:",max_num)

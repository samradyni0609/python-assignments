A= int(input("Enter number of elements:"))

list = []

total =0


for i in range(A):
    
    No= int(input())
    list.append(No)
    total = total +No

print("Addition is:", total)

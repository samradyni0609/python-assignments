import MarvellousNum

def ListPrime(list):
    
    sum = 0
    for i in list:
        
        if MarvellousNum.ChkPrime(i):
            
            sum = sum + i
    return sum

A= int(input("Enter number of elements:"))
list = []

for i in range(A):
    list.append(int(input()))

result = ListPrime(list)

print("Addition is:", result)

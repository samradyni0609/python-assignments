No=int(input("Enter a number:"))

sum = 0

for i in range(1,No):
    
    if No%i==0:
        sum=sum + i

print("Addition of factors:",sum)

def SumDigits(No):
    
    sum=0
    
    while No>0:
        
        digit = No % 10
        sum = sum + digit
        No= No // 10
        
    print(sum)

A = int(input("Enter number:"))

SumDigits(A)

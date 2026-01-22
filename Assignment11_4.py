def Reverse(No):
    
    rev=0
    
    while No>0:
        
        digit = No % 10
        rev = rev*10+ digit
        No= No // 10
        
    print(rev)

A = int(input("Enter number:"))

Reverse(A)

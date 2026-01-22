def CountDigits(No):
    
    count=0
    
    while No>0:
        count=count+1
        No= No // 10
    print(count)

A = int(input("Enter number:"))

CountDigits(A)

def ChkNum(No):
    
    if No>0:
        
        print("Positive Number")
        
    elif No<0:
        
        print("Negative Number")
        
    else:
        print("Zero")

A = int(input("Enter number:"))

ChkNum(A)

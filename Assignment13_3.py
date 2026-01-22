def ChkPerfect(No):
    
    i = 1
    Sum = 0
    
    while i < No:
        
        if No%i == 0:
            Sum = Sum + i
        
        i = i+1
    
    if Sum == No:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


A = int(input("Enter number: "))
ChkPerfect(A)

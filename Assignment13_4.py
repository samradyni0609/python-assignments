def Binary(No):
    
    binary = ""
    
    while No>0:
        binary=str(No%2) + binary
        No = No // 2
        
    print(binary)

A = int(input("Enter number:"))

Binary(A)

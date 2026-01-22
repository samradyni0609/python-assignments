def ChkPalindrome(No):
    original=No
    rev=0
    
    while No>0:
        
        digit = No % 10
        rev = rev*10+ digit
        No= No // 10
        
    if original==rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

A = int(input("Enter number:"))

ChkPalindrome(A)

No=int(input("Enter a number:"))

sum = 0

while No > 0:
    
    digit =No% 10
    sum = sum + digit
    No=No // 10

print("Addition of digits:",sum)

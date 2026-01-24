Large= lambda No1,No2,No3: No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)
A = Large(10,20,30)

print("Largest number is:",A) 
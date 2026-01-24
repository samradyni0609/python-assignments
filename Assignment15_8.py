nums = [3,5,15,20,30]

A = list(filter(lambda x: (x%3==0 and x%5==0),nums))

print("Numbers divisible by 3 and 5:",A)
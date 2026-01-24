strings = ["python","javascript","PHP"]

A = list(filter(lambda x: len(x)>5,strings))

print("Strings with length greater than 5:",A)
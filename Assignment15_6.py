from functools import reduce
nums = [1,2,3,4]
minimum = reduce(lambda x,y:x if x < y else y,nums)
print(minimum)
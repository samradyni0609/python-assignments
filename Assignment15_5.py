from functools import reduce
nums = [1,2,3,4]
maximum = reduce(lambda x,y:x if x > y else y,nums)
print(maximum)
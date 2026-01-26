import threading

def cal_sum(list,result):
    result["sum"] = sum(list)


def cal_product(list,result):
    product = 1
    
    for n in list:
        
        product *= n
        
    result["product"] = product


nums = list(map(int, input("Enter numbers:").split()))

result = {}

t1 = threading.Thread(target=cal_sum, args=(nums, result))
t2 = threading.Thread(target=cal_product, args=(nums, result))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum:",result["sum"])
print("Product:",result["product"])

import threading

def even_list(numbers):
    even_nums = []
    
    for i in numbers:
        if i%2 == 0:
            
            even_nums.append(i)

    print("Even elements:",even_nums)
    print("Sum of even elements:",sum(even_nums))


def odd_list(numbers):
    odd_nums = []
    
    for i in numbers:
        if i % 2 != 0:
            
            odd_nums.append(i)

    print("Odd elements:", odd_nums)
    print("Sum of odd elements:", sum(odd_nums))


nums= list(map(int, input("Enter numbers: ").split()))


t1 = threading.Thread(target=even_list, args=(nums,), name="EvenList")
t2 = threading.Thread(target=odd_list, args=(nums,), name="OddList")


t1.start()

t2.start()

t1.join()
t2.join()

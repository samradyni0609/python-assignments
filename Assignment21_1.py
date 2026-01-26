import threading

def is_prime(n):
    
    if n<= 1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True


def print_prime(numbers):
    
    prime= []
    
    for n in numbers:
        
        if is_prime(n):
            
            prime.append(n)
    print("Prime numbers:", prime)


def print_nonprime(numbers):
    
    nonprime = []
    for n in numbers:
        
        if not is_prime(n):
            
            nonprime.append(n)
    print("Non-prime numbers:", nonprime)


nums = list(map(int, input("Enter numbers:").split()))

t1 = threading.Thread(target=print_prime, args=(nums,), name="Prime")
t2 = threading.Thread(target=print_nonprime, args=(nums,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()

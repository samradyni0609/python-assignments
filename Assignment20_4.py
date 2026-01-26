import threading


def count_small(n):
    
    count = 0
    for ch in n:
        
        if ch.islower():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters:", count)
    print()



def count_capital(n):
    
    count = 0
    for ch in n:
        
        if ch.isupper():
            count += 1

    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Number of uppercase characters:",count)
    print()



def count_digits(n):
    
    count = 0
    for ch in n:
        
        if ch.isdigit():
            count += 1

    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Number of digits:",count)
    print()


text =input("Enter a string:")


t1 = threading.Thread(target=count_small,args=(text,),name="Small")
t2 = threading.Thread(target=count_capital,args=(text,),name="Capital")
t3 = threading.Thread(target=count_digits,args=(text,),name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

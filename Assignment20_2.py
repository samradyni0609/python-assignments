import threading


def even_factors(n):
    
    even_list = []
    
    for i in range(1, n+1):
        
        if n % i == 0 and i % 2 == 0:
            even_list.append(i)

    print("Even factors:",even_list)
    print("Sum of even factors:",sum(even_list))



def odd_factors(n):
    odd_list = []
    
    for i in range(1,n+1):
        
        if n % i == 0 and i % 2 != 0:
            odd_list.append(i)

    print("Odd factors:",odd_list)
    print("Sum of odd factors:",sum(odd_list))



num= int(input("Enter a number:"))


t1 = threading.Thread(target=even_factors,args=(num,),name="EvenFactor")
t2 = threading.Thread(target=odd_factors,args=(num,),name="OddFactor")


t1.start()
t2.start()


t1.join()
t2.join()

print("Exit from main")

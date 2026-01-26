import threading

def print_forward():
    
    print("Thread1:")
    
    for i in range(1,51):
        print(i)



def print_reverse():
    print("Thread2:")
    
    for i in range(50,0,-1):
        
        print(i)


t1 = threading.Thread(target=print_forward, name="Thread1")

t2 = threading.Thread(target=print_reverse, name="Thread2")



t1.start()
t1.join()     

t2.start()
t2.join()

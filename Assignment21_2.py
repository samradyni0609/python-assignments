import threading

def find_max(list):
    print("Maximum element:", max(list))


def find_min(list):
    print("Minimum element:", min(list))


nums = list(map(int, input("Enter numbers:").split()))

t1 = threading.Thread(target=find_max,args=(nums,),name="Thread1")
t2 = threading.Thread(target=find_min,args=(nums,),name="Thread2")

t1.start()
t2.start()

t1.join()
t2.join()

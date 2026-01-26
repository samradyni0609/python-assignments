import threading

def print_even():
    print("Even numbers:")
    for i in range(2, 21, 2):
        print(i)
def print_odd():
    print("Odd numbers:")
    for i in range(1, 20, 2):
        print(i)


even_thread = threading.Thread(target=print_even, name="Even")
odd_thread = threading.Thread(target=print_odd, name="Odd")


even_thread.start()
odd_thread.start()


even_thread.join()
odd_thread.join()

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i, end=" ")
        time.sleep(0.5)

def print_letters():
    for letter in "ABCDE":
        print(letter, end=" ")
        time.sleep(0.5)

# Example Usage
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
import threading


# Function to print even numbers
def print_even():
    for i in range(2, 21, 2):
        print(f"Even Thread: {i}")
# Function to print odd numbers
def print_odd():
    for i in range(1, 21, 2):
        print(f"Odd Thread: {i}")
# Creating threads
t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
# Starting threads
t1.start()
t2.start()

# Waiting for threads to complete
t1.join()
t2.join()

print("Threads execution completed.")

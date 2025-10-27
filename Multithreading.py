'''Multithreading in Python allows for the concurrent execution of multiple threads within a single process. This means a program can perform multiple tasks seemingly simultaneously, improving efficiency and responsiveness, particularly for I/O-bound operations. '''


import threading
import time

def task(name):
    print(f"Thread {name}: Starting")
    time.sleep(2)  # Simulate I/O-bound operation
    print(f"Thread {name}: Finishing")

# Create threads
thread1 = threading.Thread(target=task, args=("One",))
thread2 = threading.Thread(target=task, args=("Two",))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Main thread: All threads finished.")
import os
import threading
from queue import Queue


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


def write_to_file(content):
    with file_lock:
        with open('data_all.txt', 'a') as f:
            f.write(content)


directory = 'data/threading'

txt_files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')])

file_lock = threading.Lock()


def thread_function():
    while True:
        filename = file_queue.get()
        if filename is None:
            break
        content = read_file(filename)
        write_to_file(content)
        file_queue.task_done()


file_queue = Queue()

for filename in txt_files:
    file_queue.put(filename)

num_threads = 4
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=thread_function)
    thread.start()
    threads.append(thread)

file_queue.join()

for _ in range(num_threads):
    file_queue.put(None)
for thread in threads:
    thread.join()

print("Tous les sonnets ont été rassemblés dans data_all.txt.")

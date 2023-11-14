import subprocess
import threading
import time
import socket
import urllib.request

def iframe_thread(port):
    while True:
        time.sleep(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            break
        sock.close()

    from colorama import Fore, Style
    print(Fore.GREEN + "
Localtunnel Endpoint IP is:", Fore.RED, urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("
"),"
",Style.RESET_ALL)
    p = subprocess.Popen(["lt", "--port", "{}".format(port)], stdout=subprocess.PIPE)
    for line in p.stdout:
        print(line.decode(), end='')

threading.Thread(target=iframe_thread, daemon=True, args=(7860,)).start()

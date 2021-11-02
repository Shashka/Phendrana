#region IMPORTS

import threading
import time
from tqdm import tqdm
from queue import Queue
from pscanner_class import dic_port
from pscanner_class import Pscanner

#endregion
#region COLORS

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#endregion

"""
Oh god what have i done ?
This file has to be run in order to execute Phendrana's port scanning utility
You just have to enter the ip Addr of the target and the port or port range to scan 

Exemple : port = 500 will either scan the port 500 only or the 500 first port (0 to 499) depending on what type of scan you've selected

This file does nothing else but gathering input from user and passing them to Pscanner class

"""

choice = str(input("[+] Scan a port [r]ange or a [s]pecific port ?"))

while choice != "r" or choice != "R" or choice != "s" or choice != "S":

    if choice == "r" or choice == "R":

        q = Queue()
        ip_addr = str(input("[+] Enter target to scan (Default Loopback): "))
        port = int(input("[+] Enter port range : "))
        thread_nbr = int(input("[+] Enter thread to use (the more threads, the fastest will be the scan and the sorting : Max value 800) : "))

        if ip_addr == "":

            ip_addr = "127.0.0.1"

        scanner = Pscanner(ip_addr, port, thread_nbr, q)


        print("\n" + "-" * 60 + "\n")
        print("\t\t\tProbing Target : " + str(ip_addr) + " \n")
        print("-" * 60 + "\n")

        for x in range(thread_nbr):
             t = threading.Thread(target=scanner.threader)
             t.daemon = True
             t.start()

        for worker in tqdm(range(port)):
            time.sleep(0.001)
            q.put(worker)

        print("\n" + "-" * 60 + "\n")
        print("\t\t\tFINISHED, NOW SORTING RESULTS\n")
        print("-" * 60 + "\n")
        q.join()

        for key, value in sorted(dic_port.items()):

            if "OPEN" in value:

                print("PORT " + str(key) + " " + OKGREEN + str(value) + ENDC)

            else:

                print("PORT " + str(key) + " " + FAIL + str(value) + ENDC)

        #May god have mercy on your soul if you change parameter of export_csv here...
        scanner.export_csv(dic_port)
        print("[INFO] Scan Complete a csv file has been created")

        break

    elif choice == "s" or choice == "S":

        print("incomming")
        break

    else:

        choice = str(input("Choose between [r]ange or [s]ingle port please"))

#region IMPORTS
import threading
from queue import Queue
import socket

#endregion

#region VAR

print_lock = threading.Lock()
port_output = []
dic_port = {}

#endregion

"""
Pscanner class handle the port scanning utility of Phendrana.
I must admit that i fucked up somewhere since the port scanning utility wasn't supposed to be a class at the begenning.
I've created it DURING Phendrana developpement as a simple function, so it may appear that this class is a little bit 
fucked up when it come to construction and modeling but hey, it work no?

Sometimes, during port scanning this class or associated methods can shat themselves so, if you're braver than me, go ahead and try to understand why it happens, i'll be forever grateful 
By the way, If you encounter any problems with this part of Phendrana, may god have mercy on your soul, you poor bastard, since even i, don't understand how the helle this frankenstein-like class can even work.

@Functions

__init__() => Simply the class constructor
scanner()  => This method handle all the work, it creates a socket and sweeps all ports that has been selected
threader() => This method i used only to handle threading operation, since port sweeps is pretty slow, threads are used to split the work between different process
export_csv() => Do i really need to explain this one ? Ok i'll do it, it will recovers scan result in order to create a csv file and display it in the dashboard

"""

class Pscanner():

    def __init__(self, ip, port, threads, queue):

        self.ip = ip
        self.port = port
        self.threads = threads
        self.queue = queue

    def scanner(self, port):

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((self.ip, port))

            with print_lock:

                if result == 0:

                    try:

                        dic = {}
                        serviceTCP = socket.getservbyport(port, "tcp")
                        serviceUDP = socket.getservbyport(port, "udp")

                        dic[serviceTCP] = port
                        dic_port[port] = "OPEN | TCP Service " + serviceTCP + " | UDP Service " + serviceUDP
                        #print("PORT " + str(port) + "\033[91m" + " [OUVERT]" + "\033[0m")

                    except Exception as e:

                        print("[Error] Port or Protocol not found, server potentially down or protected\n")
                        pass

                else:

                    try:

                        #print("PORT " + str(port) + "\033[91m" + " [FERMÉ]" + "\033[0m")
                        port_output.append("PORT " + str(port) + " [CLOSED]")
                        dic_port[port] = "CLOSED"
                        s.close()

                    except Exception as e:

                        print("[Error] Port or Protocol not found, server potentially down or protected\n")
                        pass

        except KeyboardInterrupt as k:

            print("[INFO] Scan interrupted by operator.")

    def threader(self):

        while True:
            worker = self.queue.get()
            Pscanner.scanner(self, worker)
            self.queue.task_done()

    def export_csv(self, port_dic):

        with open("pscanresults.csv", "w") as f:

            for key in port_dic.keys():

                f.write("%s,%s\n" % (key, port_dic[key]))
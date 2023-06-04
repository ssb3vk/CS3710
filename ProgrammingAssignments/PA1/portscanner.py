# This code is based off: https://www.geeksforgeeks.org/port-scanner-using-python/

from datetime import datetime
import socket

def main():
    # method to get scan target
    scanTarget = input("Enter a target to scan: ")
    #print(scanTarget)
    
    
    print("Please enter the range of ports you would like to scan on the target")
    
    
    # method to get start port
    startPort = input("Enter a start port: ")
    #print(startPort)
    
    
    # method to get end port
    endPort = input("Enter a end port: ")
    #print(endPort)
    
    
    # print start time
    print("Scanning started at: ", datetime.now())
    # start scanning here


    # for port scanning, we just iterate over the given ports
    # (non incluseive) so we go [startPort, endPort)
    # and check all of them to see if they are open
    for port in range(int(startPort), int(endPort)): 
        # here we initialize a socket that uses the INET address family
        # and uses the a SOCK_STREAM type, which is essentially TCP
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
        
        # setting the default timeout to 10 seconds
        # can't use "socket.settimeout" so have to use setdefaulttimeout
        socket.setdefaulttimeout(10)

        # in the case that we connect (connect_ex returns 0) 
        # we just say that the port is open
        # otherwise the port is closed
        if ( s.connect_ex((scanTarget, port)) == 0 ): 
            print("Port {} is open".format(port))
        else: 
            print("Port {} is closed".format(port))

        # and we close the said socket after every attempted connection
        s.close()

if __name__ == "__main__":
    main()
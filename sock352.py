
# This is the skeleton code of a cs 352 socket
# You must change the code in the pass statements to make the client and server work. 

import socket as ip

class socket:
    
    def __init__(self):
        self.my_socket = ip.socket(ip.AF_INET, ip.SOCK_DGRAM)
        pass
       
    def socket():
        return self
    
    def bind(self,address):
        self.my_socket.bind(address)
        pass
       
    
    def sendto(self,buffer,address):
        self.my_socket.sendto(buffer, address)
        pass
   

    def recvfrom(self,nbytes):
        return self.my_socket.recvfrom(nbytes)

    def close(self):
        self.my_socket.close()
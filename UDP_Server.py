import socket
source_host = "0.0.0.0"
source_port = 3000
# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((source_host, source_port))
while True:
    # recieve data from client
    data, addr = server.recvfrom(4096)
    if len(data):
        print(addr, end=":")
        print(data)
        # send data back to client    
        server.sendto(data, addr)     
    

import socket
import sys

#create a new socket
def start_server():
        try:
            global host
            global port
            global s
            host="192.168.0.27"
            port=9999
            s=socket.socket()
            
        except socket.error as msg:
            print("Socket creation error: " + str(msg))
 # bind the socket to a server and port           
def bind():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(5)
        print("Server started on {}:{}".format(host, port))
    except socket.error as msg:
        print("Socket binding error: " + str(msg))
        bind()
        
        
#accept connections

def socket_accept():
    conn,addr=s.accept()
    print("Connection established with "+"IP- "+addr[0]+" PORT- "+str(addr[1]))
    send_message(conn)
    conn.close()
    
# send commands to the client 
def send_message(conn):
    while True:
        cmd=input()
        if cmd=="quit":
            conn.close
            s.close()
            sys.exit()
        
        if(len(str.encode(cmd)))>0:
            conn.send(str.encode(cmd))
            client_response = conn.recv(1024).decode('utf-8')
            print(client_response,end="")
            
def main():
    start_server()
    bind()
    socket_accept()
    
    
main()
            
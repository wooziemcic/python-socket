import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #using hostbyname to get the hostname of the server
HEADER = 64
#bind the socket
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #what type of IP addresses we are picking (family, type)
server.bind(ADDR) #bound this socket to the address so now anything that hits the adress with bind to the socket

def handle_client(conns, addr): #(handle the individual connection one client and one server)
    print("New Conncetion {addr} connceted.")
    connected = True
    while connected:
        msg_length = conns.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conns.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
    conns.close()


def start(): #allow server to listening to connections and handling and passing them to run in a new thread (new connections and where it needs to go)
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conns, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conns, addr))
        thread.start()
        print(f"Active conncetions {threading.activeCount() - 1}")

print("Starting the Server")
start()


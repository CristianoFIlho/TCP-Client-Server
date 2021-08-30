import socket 

if      __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    string = input("Enter a string: ")
    server.send(bytes(string, 'utf-8'))
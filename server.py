import socket

if      __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)


    while True:
        client, addr = server.accept()
        print("Client connected: {address[0]:address[1]}")


   
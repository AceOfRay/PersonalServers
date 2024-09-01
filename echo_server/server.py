import socket
import os

class Server():
    def __init__(self) -> None:
        self.PORT = 31313
        self.HOST = "127.0.0.1"

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()

            while True:    
                connection, address = s.accept()

                pid = os.fork()

                if pid == 0:
                    s.close()
                    self.handle_client(connection, address)
                    connection.close()
                    os._exit(0)
                else:
                    connection.close()
                    print(f"Client being handled by child process w/ PID = {pid}")

    def handle_client(self, connection, address):
        with connection as c:
            print(f"Connected to {address}")
            while True:
                data = c.recv(1024)
                
                if not data:
                    break

                print(f"Data Recieved and Returned: {data.decode()}")
                c.sendall(data)


if __name__ == '__main__':
    s = Server()
    s.run()
import socket

class Client:
    def __init__(self) -> None:
        self.PORT = 31313
        self.HOST = "127.0.0.1"
        self.run()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            while True:
                msg = input("Enter a message to send to the client:\n")

                if msg == "q":
                    break

                s.sendall(msg.encode())

                response = s.recv(1024).decode()
                print(response)



if __name__ == '__main__':
    Client()
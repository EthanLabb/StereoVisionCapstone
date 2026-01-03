import socket
import threading

class ImageServerHost:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.connected = False
        
    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Image server started on {self.host}:{self.port}")
        #accept single client connection
        
        client_socket, addr = self.server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(
            target=self.handle_client,
            args=(client_socket,)
        )
        self.connected = True
        client_handler.start()
            
    #send image data to client
    def handle_client(self, client_socket):
        with client_socket:
            image_data = self.get_image_data()
            client_socket.sendall(image_data)
            print("Image data sent to client")
            
class ImageClient:
    def __init__(self, server_host='localhost', server_port=8080):
        self.server_host = server_host
        self.server_port = server_port
        self.connected = False
        
    def receive_image(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.server_host, self.server_port))
            image_data = sock.recv(4096)
            print("Image data received from server")
            self.save_image(image_data)
            
    def save_image(self, image_data, filename="received_image.jpg"):
        with open(filename, 'wb') as f:
            f.write(image_data)
        print(f"Image saved as {filename}")
            
            
    
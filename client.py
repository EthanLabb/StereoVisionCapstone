from image_transfer import ImageClient
#import openCV code

class StereoClientDevice:
    def __init__(self, server_host='192.168.1.100', server_port=8080):
        self.client = ImageClient(server_host, server_port)
        #self.stereo_processor = StereoImageProcessor()
    
    def load_local_images(self, left_filename="left_image.jpg", right_filename="right_image.jpg"):
        #load images from local storage
        pass    
        
    def run(self):
        if self.client.connected:
            print("Receiving images from server...")
            self.client.receive_image()
        else:
            print("Client not connected to server, loading local images...")
            self.load_local_images()

        #process received images for depth mapping
        #self.stereo_processor.process_images("received_image.jpg")
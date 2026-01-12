from image_transfer import ImageClient
#import kevin's stereo openCV code

class StereoClientDevice:
    def __init__(self, server_host='192.168.1.100', server_port=8080):
        self.client = ImageClient(server_host, server_port)
        #self.stereo_processor = StereoImageProcessor()
    
    def load_local_images(self, left_filename="left_image.jpg", right_filename="right_image.jpg"):
        #load images from local storage
        pass    
        
    def run(self):
        self.client.connect()
        while self.client.connected:
            imgL, imgR = self.client.receive_images()
            #TODO process received images
        else:
            print("Client not connected to server, loading local images...")
            self.load_local_images()
            #process received images for depth mapping

if __name__ == "__main__":
    device = StereoClientDevice()
    device.run()
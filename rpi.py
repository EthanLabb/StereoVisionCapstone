from image_transfer import ImageServerHost
from acquisition import StereoCameraAcquisition

class RaspberryPiStereoSystem:
    def __init__(self):
        self.running = False
        
        self.server = ImageServerHost(host='192.168.1.100', port=8080)
        self.stereo_system = StereoCameraAcquisition()
        #TODO: Initialize other components like UI
        
    def save_images_locally(self, imgL, imgR, left_filename="left_image.jpg", right_filename="right_image.jpg"):
        with open(left_filename, 'wb') as fL:
            fL.write(imgL.get_array("main"))
        with open(right_filename, 'wb') as fR:
            fR.write(imgR.get_array("main"))
        print(f"Images saved locally: {left_filename}, {right_filename}")
    
    def run(self):
        self.running = True
        self.stereo_system.initialize_cameras()
        self.server.start_server()

        self.stereo_system.display_preview()

        while self.running:
            #interface with UI to take images when button pressed
            if user_presses_capture_button():
                self.stereo_system.stop_preview()
                imgL, imgR = self.stereo_system.capture_stereo_image()

                if self.server.connected:
                    print("Sending images to client...")
                    self.server.send_images()
                else: 
                    self.save_images_locally(imgL, imgR)

                self.stereo_system.display_preview()
            
    
if __name__ == "__main__":
    rpi = RaspberryPiStereoSystem()
    rpi.run()
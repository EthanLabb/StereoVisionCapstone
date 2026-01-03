from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from libcamera import controls
import time

class StereoCameraAcquisition:
    def __init__(self, left_camera_id=0, right_camera_id=1, frame_rate=30):
        self.left_camera = Picamera2(camera_num=left_camera_id)
        self.right_camera = Picamera2(camera_num=right_camera_id)
        
        self.framerate = frame_rate
        self.ctrls = {"FrameRate": self.framerate, 'SyncMode': controls.rpi.syncModeEnum.Server}

        self.left_config_still = self.left_camera.create_still_configuration(main={"size": (1920, 1080)}, controls=self.ctrls)
        self.right_config_still = self.right_camera.create_still_configuration(main={"size": (1920, 1080)}, controls=self.ctrls)
        
        self.left_config_video = self.left_camera.create_video_configuration(main={"size": (1920, 1080)}, controls=self.ctrls)
        self.right_config_video = self.right_camera.create_video_configuration(main={"size": (1920, 1080)}, controls=self.ctrls)
        
        self.encoder = H264Encoder(bitrate=1000000)
        self.encoder.sync_enable = True

    def configure_cameras(self):
        self.left_camera.configure(self.left_config_still)
        self.right_camera.configure(self.right_config_still)
        
    def start(self):
        self.left_camera.start(self.left_config_still)
        self.right_camera.start(self.right_config_still)
        time.sleep(2)  # Allow cameras to warm up
        
    def initialize_cameras(self):
        self.left_camera.stop()
        self.right_camera.stop()
        self.configure_cameras()
        self.start()

    def capture_stereo_image(self, left_filename="left_image.jpg", right_filename="right_image.jpg"):
        reqL = self.left_camera.capture_sync_request()
        reqR = self.right_camera.capture_sync_request()
        return reqL, reqR
        print(f"Captured stereo images: {left_filename}, {right_filename}")
        
    def capture_video(self, left_filename="left_video.h264", right_filename="right_video.h264", duration=10):
        self.left_camera.start_recording(self.encoder, left_filename)
        self.right_camera.start_recording(self.encoder, right_filename)
        self.encoder.sync.wait()
        time.sleep(duration)
        self.left_camera.stop_recording()
        self.right_camera.stop_recording()
        print(f"Captured stereo videos: {left_filename}, {right_filename}")
        
    def display_preview(self):
        self.left_camera.start_preview()
        self.right_camera.start_preview()
        
    def stop_preview(self):
        self.left_camera.stop_preview()
        self.right_camera.stop_preview()
        
    def stop(self):
        self.left_camera.stop()
        self.right_camera.stop()




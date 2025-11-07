from guizero import App, Text, PushButton, TextBox, Window, ButtonGroup
import numpy as np

app = App(title="Capture")


def list_cameras():
    #ethan's list_cameras adapted to guizero
    global cams_ids
    """cams = Picamera2.global_camera_info()"""

    #testing camera list
    cams=[{'Id':1,'Model':'hi1'},{'Id':3,'Model':'hi2'},{'Id':4,'Model':'hi3'}]

    cams_ids=np.zeros(len(cams),dtype=int)
    words="\nDetected cameras:\n"
    i=0
    for cam in cams:
        #instead of printing out we put it in a variable to display in a text box thingy
        words=words+(f"\n - ID: {cam['Id']} | Model: {cam['Model']}")

        #really annoying that i have to add this but it is required for the ui to be nicer™
        cams_ids[i]=cam['Id']
        i+=1
    
    #showing the camera list
    cam_list.value=words
    cam_list.show()
        

def capture_single_image():
    #new gui code
    global getfilename
    #new window
    getfilename=Window(app,title="File name")

    #gui code for the file name 
    getfilenametext=Text(getfilename,text="Enter File name")
    #text box for file name
    filenamebox=TextBox(getfilename)
    filename=filenamebox.value
    #lambda because apparently if you do just the command it'll terminate the window before you click the button ¯\_(ツ)_/¯
    finished=PushButton(getfilename, text="Finished",command=lambda: eth_capture_single_image(filename))
    

def eth_capture_single_image(filename):
   
    #ethan's picam code
    """
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file(filename)
    #print(f"[Default Camera] Saved {filename}\n")"""

    #close the filename prompt window
    getfilename.destroy()
    

def capture_from_camera():
    #new gui code
    global getfiledata
    
    #new window for user data
    getfiledata=Window(app,title="File name")
    getfilenametext=Text(getfiledata,text="Enter File name")
    
    #get file name
    filenamebox=TextBox(getfiledata)
    filename=filenamebox.value

    #get camera id
    #!!! i don't know how to force list_camera to just start all the time so you have to click it first or else you can't select a camera id
    camera_id = ButtonGroup(getfiledata, options=cams_ids)
    finished=PushButton(getfiledata, text="Finished",command=lambda: eth_capture_from_camera(filename,camera_id.value))
    
    
def eth_capture_from_camera(filename,camera_id):
    #ethan's picamcode
    """
    picam2 = Picamera2(camera_num=camera_id)
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file(filename)
    print(f"[Camera {camera_id}] Saved {filename}\n")
    """

    #close user data window
    getfiledata.destroy()
    

    
def capture_from_all():
    #ethan's picamcode
    """
    cams = Picamera2.global_camera_info()
    for cam in cams:
        cid = cam["Id"]
        filename = f"cam{cid}.jpg"
        capture_from_camera(cid, filename)
    """
    
#gui code
intro = Text(app, text="Raspberry Pi Camera Controller")

#gui code for buttons
List_cameras = PushButton(app, text="List cameras",command=list_cameras)
CapImgDefcam = PushButton(app, text="Capture image (default camera)",command=capture_single_image)
CapImgSelcam = PushButton(app, text="Capture image from specific camera",command=capture_from_camera)
CapImgAllcam = PushButton(app, text="Capture one image from every camera",command=capture_from_all)
exit = PushButton(app, text="Exit", command=app.destroy)

#hide the camera list until needed
cam_list=Text(app, text="")
cam_list.hide()


app.display()
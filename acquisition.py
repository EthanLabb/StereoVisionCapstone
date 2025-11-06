from picamera2 import Picamera2
import time


def list_cameras():
    cams = Picamera2.global_camera_info()
    print("\nDetected cameras:")
    for cam in cams:
        print(f" - ID: {cam['Id']} | Model: {cam['Model']}")
    print()
    return cams


def capture_single_image(filename="image.jpg"):
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file(filename)
    print(f"[Default Camera] Saved {filename}\n")


def capture_from_camera(camera_id, filename="image.jpg"):
    picam2 = Picamera2(camera_num=camera_id)
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file(filename)
    print(f"[Camera {camera_id}] Saved {filename}\n")


def capture_from_all():
    cams = Picamera2.global_camera_info()
    for cam in cams:
        cid = cam["Id"]
        filename = f"cam{cid}.jpg"
        capture_from_camera(cid, filename)


def main():
    while True:
        print("================================")
        print(" Raspberry Pi Camera Controller ")
        print("================================")
        print("1. List cameras")
        print("2. Capture image (default camera)")
        print("3. Capture image from specific camera")
        print("4. Capture one image from every camera")
        print("5. Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            list_cameras()

        elif choice == "2":
            filename = input(
                "Output filename (default: default.jpg): ") or "default.jpg"
            capture_single_image(filename)

        elif choice == "3":
            cams = list_cameras()
            cam_id = int(input("Enter camera ID: "))
            filename = input(
                "Output filename (default: output.jpg): ") or "output.jpg"
            capture_from_camera(cam_id, filename)

        elif choice == "4":
            capture_from_all()

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()

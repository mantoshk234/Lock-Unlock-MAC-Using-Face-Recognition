import cv2  # import OpenCV

import config
from utils.app_constants import *
from utils.utils import assure_clean_path_exists


class FaceDataBase:
    def __init__(self):
        # Start video capturing
        self.vid_cam = cv2.VideoCapture(0)

        # Detect object in video stream using Haarcascade Frontal Face
        self.face_cascade = cv2.CascadeClassifier(config.CFG[FACE_POINT_DETECTION_DATA])

        self.face_id = 1  # For each person, there will be one face id
        self.count = 0  # Initialize sample face image

        assure_clean_path_exists(config.CFG[IMAGE_DATA_DIR])

    def capture_face_images(self):
        print("PLEASE LOOK INTO CAMERA - MOVE YOUR FACE IN DIFFERENT ANGLES")
        print("Please have patience, application is taking your pictures")
        while True:
            # Capture video frame _, is used to ignored first value because vid_cam.read() is returning 2 values
            _, image_frame = self.vid_cam.read()

            # Convert frame to grayscale
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # Detect faces using Cascade Classifier(xml file)
            faces = self.face_cascade.detectMultiScale(gray, 1.4, 5)

            for (x, y, w, h) in faces:
                # Crop the image frame into rectangle
                cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Increment face image
                self.count += 1

                # Save the captured image into the IMAGE_DATA_DIR folder
                cv2.imwrite(config.CFG[IMAGE_DATA_DIR] + "/User." + str(self.face_id) + '.' + str(self.count) + ".jpg",
                            gray[y:y + h, x:x + w])

                # Display the video frame, with rectangular box on the person's face
                cv2.imshow('Creating Dataset!!!', image_frame)

            # To stop taking video, press 'Esc'
            if cv2.waitKey(100) & 0xFF == 27:
                break

            # If image taken reach 300, stop taking video
            elif self.count > config.CFG[TRAINING_IMAGE_COUNT]:
                break

        # Stop video
        self.vid_cam.release()

        # Close all windows
        cv2.destroyAllWindows()

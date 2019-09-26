import subprocess
import time

import Quartz
import cv2

import config
from utils.app_constants import *


class SystemLocker:
    def __init__(self):
        self.MAX_COUNTER_CORRECT = 5
        self.counter_correct = 0  # counter variable to count number of times loop runs

        self.MAX_COUNTER_WRONG = 3
        self.counter_wrong = 0

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.recognizer.read(config.CFG[TRAINING_DATA] + "/trainer.yml")  # load training model
        self.cascadePath = config.CFG[FACE_POINT_DETECTION_DATA]  # cascade path

        self.faceCascade = cv2.CascadeClassifier(self.cascadePath)  # load cascade

        self.font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style

        self.cam = cv2.VideoCapture(0)

    def lock_screen(self):
        # https://www.reddit.com/r/Python/comments/2rrb29/need_a_way_to_lock_and_unlock_macbook_screen_with/
        subprocess.call('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend',
                        shell=True)

    def is_mac_locked(self):
        d = Quartz.CGSessionCopyCurrentDictionary()
        # If the dictionary has CGSSessionScreenIsLocked = 1, the screens are locked.
        is_locked = d.get("CGSSessionScreenIsLocked", 0)
        return False if is_locked == 0 else True

    def lock_unlock_system(self):
        while True:
            if self.is_mac_locked():
                self.counter_correct = self.counter_wrong = 0
                time.sleep(config.CFG[LOCK_TIME] * 2)
                continue

            _, im = self.cam.read()

            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:

                cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)

                # Recognize the face belongs to which ID
                Id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])

                if confidence > 80:  # confidence usually comes greater than 80 for strangers
                    print("Stranger face is detected")
                    self.counter_wrong += 1
                    Id = "Unknown + {0:.2f}%".format(round(100 - confidence, 2))
                    cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)
                    cv2.putText(im, str(Id), (x, y - 40), self.font, 1, (0, 0, 0), 2)
                else:  # confidence usually comes less than 80 for correct user(s)
                    print("Known face is detected")
                    Id = "Saksham + {0:.2f}%".format(round(100 - confidence, 2))
                    self.counter_correct += 1
                    # self.counter_wrong -= 1
                    cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (255, 255, 255), -1)
                    cv2.putText(im, str(Id), (x, y - 40), self.font, 1, (0, 0, 0), 2)

                if self.counter_wrong == self.MAX_COUNTER_WRONG:
                    print("System is locked")
                    self.counter_correct = self.counter_wrong = 0
                    self.lock_screen()
                    break

                # if counter = 6 then program will terminate as it has recognized correct user for 6 times.
                if self.counter_correct == self.MAX_COUNTER_CORRECT:
                    print("face of this computer's user successfully recognised")
                    self.counter_wrong -= 2
                    self.counter_correct = 0

            # If 'Esc' is pressed, terminate the  program
            if cv2.waitKey(100) & 0xFF == 27:
                break

            time.sleep(config.CFG[LOCK_TIME])

        self.cam.release()

        cv2.destroyAllWindows()


sL = SystemLocker()
sL.lock_unlock_system()

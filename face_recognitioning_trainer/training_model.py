import os

import cv2
import numpy as np  # numpy for matrix calculations
from PIL import Image

import config
from utils.app_constants import *
from utils.utils import assure_clean_path_exists


class FaceTrainer:
    def __init__(self):
        # Create Local Binary Patterns Histograms for face recognization
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier(config.CFG[FACE_POINT_DETECTION_DATA])

    def getImagesAndLabels(self, path):
        """
        getImagesAndLabels method gets the images and label data
        :param path:
        :return: list of images and list of ints
        """

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # Get all file path

        faceSamples = []  # create empty face sample list

        ids = []  # create empty id list

        for imagePath in imagePaths:  # Loop for all the file path

            PIL_img = Image.open(imagePath).convert('L')  # Get the image and convert it to grayscale

            img_numpy = np.array(PIL_img, 'uint8')  # PIL image to numpy array

            id = int(os.path.split(imagePath)[-1].split(".")[1])  # Get the image id

            faces = self.detector.detectMultiScale(img_numpy)  # Get the face from the training images

            for (x, y, w, h) in faces:  # Loop for each face, append to their respective ID

                faceSamples.append(img_numpy[y:y + h, x:x + w])  # Add the image to face samples

                ids.append(id)  # Add the ID to IDs

        return faceSamples, ids

    def train_app_with_pics(self):
        print("Please have patience, Application is training itself with your pictures")
        # Get the faces and IDs
        faces, ids = self.getImagesAndLabels(config.CFG[IMAGE_DATA_DIR])

        # Train the model using the faces and IDs
        self.recognizer.train(faces, np.array(ids))

        assure_clean_path_exists(config.CFG[TRAINING_DATA])

        # Save the model into trainer.yml
        self.recognizer.save(config.CFG[TRAINING_DATA] + "/trainer.yml")

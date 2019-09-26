from face_recognitioning_trainer.create_face_datasets import FaceDataBase
from face_recognitioning_trainer.training_model import FaceTrainer

# capture 400 images of yours, move around little bit by giving angles
fd = FaceDataBase()
fd.capture_face_images()

# Training the app for your face
ft = FaceTrainer()
ft.train_app_with_pics()

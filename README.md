# KI-hacks-2-Lock-Unlock-MAC-Using-Face-Recognition

Reference: https://github.com/saksham-jain/Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition

sudo -H pip3 install -r requirements.txt

export PYTHONPATH=$PWD

# Run this to capture 300 images of yours, move around little bit by giving angles

# Training the app for your face
python3 scripts/create_face_datasets_and_train_app.py

# lock_unlock_face_recognition
python3 scripts/lock_unlock_face_recognition.py


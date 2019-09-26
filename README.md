# KI-hacks-2-Lock-Unlock-MAC-Using-Face-Recognition

Reference: https://github.com/saksham-jain/Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition

# How to install dependencies
 - cd Lock-Unlock-MAC-Using-Face-Recognition
 - sudo -H pip3 install -r requirements.txt

# How to run the application
- cd Lock-Unlock-MAC-Using-Face-Recognition
- export PYTHONPATH=$PWD
- Run this to capture 300 images of yours, move around little bit by giving angles and to train the app for your face. This runs to be only once.
    - python3 scripts/create_face_datasets_and_train_app.py

- Run this script whenever you would like to launch the application to auto lock your system based on face recognition
    - python3 scripts/lock_unlock_face_recognition.py


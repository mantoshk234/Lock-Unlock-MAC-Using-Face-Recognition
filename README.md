# Lock-Unlock-MAC-Using-Face-Recognition

Youtube Demo: https://youtu.be/3Y66c7gPQL8

Python3.6 is required.

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

## Inspiration
I have observed a few of my colleagues in the past, and also in present forget to lock their system while going somewhere. In some cases, this could not be safe.

## What it does
It locks the MAC once it detects that you are not sitting in front of your system or a stranger is sitting in front of system.

## What I learned
Solutions do not need to be complex to solve a problem.

## What's next for Lock-Unlock-MAC-Using-Face-Recognition
Algorithm to decide lock time could be optimized and also this application could be made portable over other OS as well.

# Reference
https://github.com/saksham-jain/Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition



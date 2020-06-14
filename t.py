import cv2
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def create_tempdir(filename):
    try:
        os.mkdir('./{}/'.format(filename))
    except OSError as e:
        print(e)

def load_video(video):
    cap = cv2.VideoCapture(video)
    if not cap:
        print("Failed to load video.")
        sys.exit(1)
    fps = cap.get(cv2.CAP_PROP_FPS)
    return cap, fps

def frames_to_png(cap):
    f = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            f += 1

            # Convert cv2 image to rgb and load from numpy array
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)

            # Convert back to bgr numpy array and write to disk
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            cv2.imwrite('./frame{}.png'.format(str(f)),frame)
        else:
            break
    cap.release()
	
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f1=filename.rsplit("/",1)
print(filename)
print(f1[1])
create_tempdir(f1[1])
os.chdir('./{}/'.format(f1[1]))
stream, framerate = load_video(filename)
frames_to_png(stream)
import os
import cv2
import numpy as np
import vidaug.augmentors as va

dataset_dir = './dataset'
sometimes = lambda aug: va.Sometimes(0.5, aug) # Used to apply augmentor with 50% probability

for category in os.listdir(dataset_dir):
    category_path = os.path.join(dataset_dir, category)
    for video in os.listdir(category_path):
        video_path = os.path.join(category_path, video)
        if video_path.is_dir():
            continue

        # loop the original video
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_size = (width, height)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        frames = []
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frames.append(frame)
            else:
                break
        cap.release()
        seq = va.Sequential([sometimes(va.InvertColor()),
                            sometimes(va.Salt()),
                            sometimes(va.Pepper()), 
                            va.HorizontalFlip(),
                            va.RandomRotate(degrees=(-10, 10)),
                            va.RandomTranslate(x=(-20, 20), y=(-20, 20)),
                            va.RandomBrightness((0.5, 2.0)),
                            va.RandomContrast((0.5, 2.0))])
        #augment the frames
        video_aug = seq(frames)

        # output the video
        out = cv2.VideoWriter(os.path.join(category_path, f"{len([file for file in os.listdir(category_path)])}.mp4v"), fourcc, fps, frame_size)
        for frame in video_aug:
            out.write(frame)
        out.release()


    
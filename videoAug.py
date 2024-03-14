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
        if not os.path.isdir(video_path):
            continue
        
        folder_name = f"{category}_{len([file for file in os.listdir(category_path)])}"
        os.makedirs(os.path.join(category_path, folder_name), exist_ok=True)
        frames = [] 
        for frame in os.listdir(video_path):
            frame_path = os.path.join(video_path, frame)
            img = cv2.imread(frame_path, cv2.IMREAD_COLOR)
            frames.append(img)
        
        seq = va.Sequential([sometimes(va.HorizontalFlip()),
                            sometimes(va.RandomShear(-0.1, 0.1)),
                            sometimes(va.RandomTranslate(5, 5))])
        #augment the frames
        # print(img[0].shape)
        img_aug = seq(frames)
        for frame in img_aug:
            # output the video
            cv2.imwrite(os.path.join(os.path.join(category_path, folder_name), f"frame_{str(len([file for file in os.listdir(os.path.join(category_path, folder_name))])).zfill(3)}.jpg"), frame)



    
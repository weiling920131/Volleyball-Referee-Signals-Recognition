import os
import random
import shutil

root_path = ".\\dataset"

new_train_path = ".\\train"
new_val_path = ".\\val"

dirs = os.listdir(root_path)
for dir in dirs:
    dir_path = os.path.join(root_path, dir)
    if os.path.isdir(dir_path):
        imgs = os.listdir(dir_path)
        img_cnt = 0

        for img in imgs:
            img_path = os.path.join(dir_path, img)
            if os.path.isdir(img_path):
                img_cnt += 1

        num_ones = int(0.8 * img_cnt)
        num_zeros = img_cnt - num_ones

        randIdx = [1] * num_ones + [0] * num_zeros

        i = 0
        for img in imgs:
            img_path = os.path.join(dir_path, img)
            if os.path.isdir(img_path):
                if randIdx[i]:
                    new_path = os.path.join(new_train_path, img)
                else:
                    new_path = os.path.join(new_val_path, img)

                shutil.copytree(img_path, new_path)
                i += 1
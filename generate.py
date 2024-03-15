import os
import random
import shutil
import csv

root_path = ".\\dataset_aug"

new_train_path = ".\\train_aug"
new_val_path = ".\\val_aug"

train_csv_path = ".\\train_aug.csv"
val_csv_path = ".\\val_aug.csv"

train_csv = open(train_csv_path, "w", newline='')
val_csv = open(val_csv_path, "w", newline='')

train_csv_writer = csv.writer(train_csv)
val_csv_writer = csv.writer(val_csv)

dirs = os.listdir(root_path)
for n in range(len(dirs)):
    dir_path = os.path.join(root_path, dirs[n])
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
                    train_csv_writer.writerow([img, dirs[n], n])
                else:
                    new_path = os.path.join(new_val_path, img)
                    val_csv_writer.writerow([img, dirs[n], n])

                shutil.copytree(img_path, new_path)
                i += 1
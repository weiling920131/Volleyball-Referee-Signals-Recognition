import numpy as np
import cv2
import os

def extract_frames(video_path, output_dir):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize frame counter
    cnt = 1
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT) / 30)
    
    # Read the first frame
    success, frame = video.read()
    
    while success:
        # Save the frame as an image
        # if cnt < frame_count:
        #     success, frame = video.read()
        #     continue

        output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(output_path, frame)
        
        # Read the next frame
        for _ in range(frame_count):
            success, frame = video.read()
            cnt += 1
            if not success:
                break


if __name__ == "__main__":
    # Example usage
    dataset_dir = "./dataset"
    for catagory in os.listdir(dataset_dir):
        cnt = 1
        catagory_path = os.path.join(dataset_dir, catagory)
        for video in catagory_path:
            video_path = os.path.join(catagory_path, video)
            extract_frames(video_path, os.path.join(video_path, f"{catagory}_{cnt}"))
            print("done")
            cnt += 1


import numpy as np
import cv2
import os

def extract_frames(video_path, output_dir, frame_interval=1):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize frame counter
    frame_count = 0
    
    # Read the first frame
    success, frame = video.read()
    
    while success:
        # Save the frame as an image
        output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(output_path, frame)
        
        # Read the next frame
        for _ in range(frame_interval):
            success, frame = video.read()
            frame_count += 1
            if not success:
                break


if __name__ == "__main__":
    # Example usage
    videos_dir = "/path/to/video.mp4"
    output_dir = "./dataset"
    frame_interval = 1
    cnt = 1
    for video_path in os.listdir(videos_dir):
        output_dir = os.path.join(output_dir, f"w{cnt}")
        extract_frames(video_path, output_dir, frame_interval)
        print("done")
        cnt += 1
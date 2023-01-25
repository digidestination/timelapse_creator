import cv2
import os
from tqdm import tqdm

video_folder = input("Enter the path to your video directory: ")
videos = []

for f in os.listdir(video_folder):
    if f.endswith('.mp4'):
        videos.append(f)

print("The following videos will be merged:")
print(videos)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_filename = "merged_videos.mp4"

# Get the dimensions of the first video to set the dimensions of the output video
cap = cv2.VideoCapture(os.path.join(video_folder, videos[0]))
width = int(cap.get(3))
height = int(cap.get(4))
cap.release()

out = cv2.VideoWriter(output_filename, fourcc, 24.0, (width,height))

for video in tqdm(videos):
    cap = cv2.VideoCapture(os.path.join(video_folder, video))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()

out.release()
print("Video merging complete.")

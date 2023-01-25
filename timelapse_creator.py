import cv2
import os
from tqdm import tqdm

image_folder = input("Enter the path to your images directory: ")
images = []

for f in tqdm(sorted(os.listdir(image_folder))):
    if f.endswith('.jpg'):
        img = cv2.imread(os.path.join(image_folder, f))
        if img is not None:
            images.append(img)
    else:
        print(f"{f} is not a jpeg file.")

first_file_name = os.path.splitext(os.listdir(image_folder)[0])[0]
last_file_name = os.path.splitext(os.listdir(image_folder)[-1])[0]
filename = first_file_name + '_until_' + last_file_name + '.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(filename, fourcc, 24.0, (images[0].shape[1],images[0].shape[0]))

for img in tqdm(images):
    out.write(img)

out.release()
print("Video creation complete.")

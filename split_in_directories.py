import os
import shutil

image_folder = input("Enter the path to your CCTV images directory: ")
images = sorted(os.listdir(image_folder))

count = 0
folder_count = 1

for i, img in enumerate(images):
    if count == 0:
        first_file_name = os.path.splitext(img)[0]
        folder_name = os.path.join(image_folder, f"{first_file_name}_folder_{folder_count}")
        os.makedirs(folder_name)
    count += 1
    shutil.move(os.path.join(image_folder, img), os.path.join(folder_name, img))
    if count == 2500 or i == len(images)-1:
        count = 0
        folder_count += 1

print("Images sorted and split into folders.")
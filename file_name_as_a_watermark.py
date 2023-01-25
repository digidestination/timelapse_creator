import cv2
import os
from tqdm import tqdm

# Specify the folder containing the images
image_folder = input("Enter the path to your images directory: ")

# Get the list of images in the folder
images = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

for image_name in tqdm(images):
    # Read the image
    img = cv2.imread(os.path.join(image_folder, image_name))
    if img is not None:
        # Get the image name without the file suffix
        file_name = os.path.splitext(image_name)[0]
        # Set the font and font size for the watermark
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        # Get the size of the text
        (text_width, text_height), _ = cv2.getTextSize(file_name, font, fontScale=font_scale, thickness=1)
        # Set the position of the watermark
        text_x = img.shape[1] - text_width - 10
        text_y = img.shape[0] - 10
        # Add the watermark to the image
        cv2.putText(img, file_name, (text_x, text_y), font, font_scale, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        # Save the image with the watermark
        cv2.imwrite(os.path.join(image_folder, image_name), img)
    else:
        print(f"{image_name} is not a valid image.")

print("Watermark added to all images.")
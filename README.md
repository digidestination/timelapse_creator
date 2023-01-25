# timelapse_creator



# Watermark images
## file_name_as_a_watermark.py
This script is used to add a watermark with the image name without file suffix on each image bottom right corner of a folder containing images. It will then save the images in the same folder.

The script begins by asking the user to input the path to the folder containing the images. It then creates a list of images in the specified folder, filtering only for jpeg images and sorting them by name.

The script then goes through each image in the list using a for loop and a progress bar from tqdm. It adds the watermark to each image using the OpenCV library, and saves the image with the same name.

At the end of the script, it will print a message indicating that the watermarking is complete.

Please note that this script will overwrite the original images in the folder. It is important to make a backup of your images before running this script.
You need to install opencv and tqdm python library to run this script.

# Create timelapse video
## timelapse_creator.py

This script is used to create a timelapse video from a folder containing jpeg images. The script will sort the images by name, and then create a video using these images. The video will have a name that is constructed from the first and last image name, with "until" in between. The script is written in python, using the OpenCV library for image processing and the tqdm library for the progress bar.

The script begins by asking the user to input the path to the folder containing the images. It then creates a list of images in the specified folder, filtering only for jpeg images and sorting them by name.

The script then gets the first and last image name, and constructs the video name from it. It sets the codec and the framerate for the video, and creates a video writer object.

The script then goes through each image in the list using a for loop and a progress bar from tqdm. It adds each image to the video writer object, and at the end of the loop, it releases the video writer object and saves the video.

At the end of the script, it will print a message indicating that the video creation is complete.

Please note that this script will create a new video file in the image folder with specified name
It is important to make a backup of your images before running this script.
You need to install opencv and tqdm python library to run this script.

This script is useful for creating timelapse videos from a large number of images, providing an easy way to view a large amount of data in a condensed format.

# Sort and split CCTV images to separate directories
## split_in_directories.py
This script is designed to sort and split a large number of CCTV images into separate directories. The user is prompted to enter the path to their CCTV images directory, and the script then proceeds to sort the images in ascending order by name using the sorted() function.

The script uses a counter variable count to keep track of the number of images in each directory, and another variable folder_count to keep track of the number of directories created. The script then uses a for loop to iterate through each image in the directory.

When the script encounters the first image in a new directory, it uses the os.path.splitext() function to extract the file name without the suffix, and creates a new directory with a name in the format {first_file_name}_folder_{folder_count}.

The script then uses the shutil.move() function to move the current image into the new directory, and increments the count variable by 1. When the count variable reaches 2500 or the loop reaches the last image, the script resets the count variable to 0 and increments the folder_count variable by 1, starting a new directory.

Once the loop has finished, the script prints a message to the console to confirm that the images have been sorted and split into folders.

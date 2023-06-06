import cv2
import os

image_folder = input("Images Folder: ")
output_path = input("Output File: ")

image_files = sorted(os.listdir(image_folder))  # Get the list of image files in the folder
frame = cv2.imread(os.path.join(image_folder, image_files[0]))  # Read the first image to get dimensions
height, width, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Specify the codec for the output video
video_writer = cv2.VideoWriter(output_path, fourcc, 30, (width, height))

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)  # Write the frame to the video

video_writer.release()  # Release the video writer
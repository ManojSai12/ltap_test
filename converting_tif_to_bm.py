
import os
import cv2
import numpy as np

# Directory paths
input_dir = "C:\\Users\\Manoj\\Desktop\\s_imgs"  # Replace with the path to your input TIFF images directory
output_dir = "C:\\Users\\Manoj\\Desktop\\b_imgs"  # Replace with the path to the output directory

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Threshold value (adjust as needed)
threshold_value = 200  # You may need to adjust this value based on your images

# Function to convert a single image to a binary mask
def image_to_binary_mask(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding to create a binary mask
    _, binary_mask = cv2.threshold(image, threshold_value, 1, cv2.THRESH_BINARY)
    binary_mask[binary_mask == 1] = 1

    # Save the binary mask
    cv2.imwrite(output_path, binary_mask * 255)

# Iterate through TIFF images in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".TIFF"):
        # Construct full paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".TIFF", "_mask.TIFF"))

        # Convert the image to a binary mask
        image_to_binary_mask(input_path, output_path)

print("Binary masks generated and saved in:", output_dir)
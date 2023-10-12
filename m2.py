import os
import numpy as np
from skimage import io

# Define the directories for composite and binary images
composite_dir = "C:\\Users\\Manoj\\Desktop\\output_binary_maps\\jan_c.TIFF"
binary_dir = "C:\\Users\\Manoj\\Desktop\\bm_imgs"
months=['jan']
# Create a dictionary to store occurrences of 255 for each year
yearly_255_counts = {}

# Loop through the years (2000 to 2023)
for year in range(2000, 2024):
    # Initialize the count for the current year to 0
    yearly_255_count = 0

    for month in months:
        # Skip specific months that you don't have images for
        if year == 2000 and month == 1:
            continue
        if year == 2023 and month in [9, 10, 11, 12]:
            continue

        # Create file paths for the composite and binary images
        composite_path = os.path.join(composite_dir)

        try:
            # Construct the corresponding binary image filename
            binary_filename = f"{month}{year}_mask.TIFF"
            binary_path = os.path.join(binary_dir, binary_filename)

            # Load images using skimage
            composite_image = io.imread(composite_path)
            binary_image = io.imread(binary_path)

            # Check if image dimensions match
            if composite_image.shape != binary_image.shape:
                print(f"Image dimensions do not match for {year}{month}, skipping...")
                continue

            # Compare each pixel in the composite and binary images
            for x in range(composite_image.shape[0]):
                for y in range(composite_image.shape[1]):
                    if composite_image[x, y] == 255 and binary_image[x, y] == 255:
                        yearly_255_count += 1

        except FileNotFoundError:
            print(f"Images not found for {year}-{month}, skipping...")

    # Store the yearly count in the dictionary
    yearly_255_counts[year] = yearly_255_count

# Display the occurrences of pixel value 255 for each year
for year, count in yearly_255_counts.items():
    print(f"Year {year}: {count} occurrences of pixel value 255")

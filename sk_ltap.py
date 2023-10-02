import os
import numpy as np
from skimage import io

# Specify the directory where your binary mask images are stored
root_directory = "C:\\Users\\Manoj\\Desktop\\bm_imgs"
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Define the weights for each year (2000 to 2023)
weights = {year: year - 2000 + 1 for year in range(2000, 2024)}

# Initialize an empty array for the final weighted sum result
weighted_sum = None

for year in range(2000, 2024):
    for month in months:
        # Construct the filename for each month and year
        filename = f"{month}{year}_mask.TIFF"  # Adjust the file extension as needed
        image_path = os.path.join(root_directory, filename)

        # Try to load the mask image, and if it fails, continue to the next month
        try:
            mask = np.array(io.imread(image_path))
        except FileNotFoundError:
            print(f"Image not found for {filename}. Skipping...")
            continue

        # Check if the pixel value is zero
        if np.any(mask):
            # Initialize or update the weighted sum
            if weighted_sum is None:
                weighted_sum = mask * weights[year]
            else:
                weighted_sum += mask * weights[year]

# Print the final weighted sum
print(weighted_sum)

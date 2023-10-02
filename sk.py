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

# Calculate the threshold value as the sum of weighted values of the last 13 years (2011 to 2023)
last_13_years_weights = [weights[year] for year in range(2011, 2024)]
threshold_value = sum(last_13_years_weights)

# Create a boolean array where True represents a cloudy area and False represents a cloud-free area
cloudy_area = weighted_sum >= threshold_value


binary_map = np.zeros_like(weighted_sum)

# Set the pixels classified as cloud-free to 1
binary_map[~cloudy_area] = 1

# Print the binary map
print(binary_map)





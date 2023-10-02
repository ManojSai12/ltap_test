import os
import numpy as np
from skimage import io

# Specify the directory where your binary mask images are stored
root_directory = "C:\\Users\\Manoj\\Desktop\\bm_imgs"
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Initialize an empty dictionary to store the sums for each year
yearly_sums = {}

for year in range(2000, 2024):
    # Initialize an empty array for the sum of pixel values for the current year
    year_sum = None

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

        # Initialize or update the pixel sum for the current year
        if year_sum is None:
            year_sum = mask
        else:
            year_sum += mask

    # Store the sum of pixel values for the current year in the dictionary
    yearly_sums[year] = np.sum(year_sum)

# Print the sums of pixel values separately for each year
for year, pixel_sum in yearly_sums.items():
    print(f"Year {year}: Pixel Sum = {pixel_sum}")

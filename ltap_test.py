import os
import numpy as np
from PIL import Image

# List of months
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Directory containing your binary mask images
mask_directory = "C:\\Users\\Manoj\\Desktop\\bm_imgs"

# Assign weights to the years with int64 data type
year_weights = {str(year): np.int64(weight) for year, weight in zip(range(2000, 2024), range(1, 25))}

# Initialize an empty array to store the weighted sum of pixel values
weighted_sum = None

# Load and process the binary mask images
for year in range(2000, 2024):
    for month in months:
        # Construct the filename for each month and year
        filename = f"{month}{year}_mask.TIFF"  # Adjust the file extension as needed
        image_path = os.path.join(mask_directory, filename)

        # Try to load the mask image, and if it fails, continue to the next month
        try:
            mask = np.array(Image.open(image_path))
        except FileNotFoundError:
            print(f"Image not found for {filename}. Skipping...")
            continue

        # Initialize or update the weighted sum
        if weighted_sum is None:
            weighted_sum = mask.astype(np.int64) * year_weights[str(year)]
        else:
            weighted_sum += mask.astype(np.int64) * year_weights[str(year)]

        # Update weight for the next year
        year_weights[str(year)] *= year_weights.get(str(year - 1), 1)

# Define a threshold value (adjust as needed)
threshold = 1000

# Apply a threshold to determine cloud-free and cloudy areas
cloud_free_areas = weighted_sum > threshold
cloudy_areas = ~cloud_free_areas
print(weighted_sum)
print(cloud_free_areas)
# The `cloud_free_areas` and `cloudy_areas` arrays now represent the predicted areas
# that are likely cloud-free and cloudy for future months.

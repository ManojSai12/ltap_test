import os
import numpy as np
import pandas as pd
from skimage import io

# Specify the directory where your composite binary maps are stored
composite_directory = "C:\\Users\\Manoj\\Desktop\\output_binary_maps"

# Specify the directory where your binary mask images are stored
binary_mask_directory = "C:\\Users\\Manoj\\Desktop\\bm_imgs"

# List of months
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Define a function to calculate pixel-wise absolute difference between two images
def calculate_pixel_difference(image1, image2):
    return np.abs(image1.astype(int) - image2.astype(int))

# Create an empty list to store the results as dictionaries
results_list = []

# Image dimensions
image_height = 360
image_width = 720

# Iterate through each month
for month in months:
    # Load the composite binary map for the current month
    composite_image_path = os.path.join(composite_directory, f"{month}_composite_binary_map.TIFF")
    composite_image = np.array(io.imread(composite_image_path))

    # Iterate through each year (binary mask images)
    for year in range(2000, 2024):
        # Construct the filename for the binary mask image
        binary_mask_image_filename = f"{month}{year}_mask.TIFF"
        binary_mask_image_path = os.path.join(binary_mask_directory, binary_mask_image_filename)

        # Check if the binary mask image file exists
        if not os.path.exists(binary_mask_image_path):
            continue

        # Load the corresponding binary mask image
        binary_mask_image = np.array(io.imread(binary_mask_image_path))

        # Ensure that both images have the same dimensions
        if composite_image.shape == (image_height, image_width) and binary_mask_image.shape == (image_height, image_width):
            # Calculate pixel-wise absolute difference
            pixel_diff = calculate_pixel_difference(composite_image, binary_mask_image)

            # Calculate the maximum possible pixel difference
            max_pixel_difference = image_height * image_width * 255  # Assuming 0 and 255 are the pixel value range

            # Normalize the pixel difference
            normalized_pixel_diff = pixel_diff / max_pixel_difference

            # Calculate the total pixel difference
            total_pixel_difference = np.sum(normalized_pixel_diff)

            # Create a dictionary with the results
            result_dict = {
                "Month": month,
                "Composite Image": f"{month}_composite_binary_map.TIFF",
                "Binary Mask Image": binary_mask_image_filename,
                "Pixel Difference": total_pixel_difference
            }

            # Append the result dictionary to the list
            results_list.append(result_dict)

# Convert the list of dictionaries to a DataFrame
results_df = pd.DataFrame(results_list)

# Save the results as a CSV file
results_csv_path = "comparison_results.csv"
results_df.to_csv(results_csv_path, index=False)
print(f"Comparison results saved to {results_csv_path}")

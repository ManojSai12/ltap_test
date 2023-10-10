# import os
# import numpy as np
# import pandas as pd
# from skimage import io, metrics

# # Specify the directory where your composite binary maps are stored
# composite_directory = "C:\\Users\\Manoj\\Desktop\\output_binary_maps"

# # Specify the directory where your binary mask images are stored
# binary_mask_directory = "C:\\Users\\Manoj\\Desktop\\bm_imgs"

# # List of months
# months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# # Define a function to calculate SSIM between two images
# def calculate_ssim(image1, image2):
#     return metrics.structural_similarity(image1, image2, multichannel=False)

# # Create an empty list to store the results as dictionaries
# results_list = []

# # Iterate through each month
# for month in months:
#     # Load the composite binary map for the current month
#     composite_image_path = os.path.join(composite_directory, f"{month}_composite_binary_map.TIFF")
#     composite_image = np.array(io.imread(composite_image_path))

#     # Construct the filename for the corresponding binary mask image
#     binary_mask_image_filename = f"{month}2023_mask.TIFF"
#     binary_mask_image_path = os.path.join(binary_mask_directory, binary_mask_image_filename)

#     # Check if the binary mask image file exists
#     if not os.path.exists(binary_mask_image_path):
#         continue

#     # Load the corresponding binary mask image
#     binary_mask_image = np.array(io.imread(binary_mask_image_path))

#     # Ensure that both images have the same dimensions
#     if composite_image.shape == binary_mask_image.shape:
#         # Calculate SSIM
#         ssim_value = calculate_ssim(composite_image, binary_mask_image)

#         # Create a dictionary with the results
#         result_dict = {
#             "Month": month,
#             "Composite Image": f"{month}_composite_binary_map.TIFF",
#             "Binary Mask Image": binary_mask_image_filename,
#             "SSIM": ssim_value
#         }

#         # Append the result dictionary to the list
#         results_list.append(result_dict)

# # Convert the list of dictionaries to a DataFrame
# results_df = pd.DataFrame(results_list)

# # Save the results as a CSV file
# results_csv_path = "ssim_results.csv"
# results_df.to_csv(results_csv_path, index=False)
# print(f"SSIM results saved to {results_csv_path}")


import os
from skimage import io, color, metrics

# Define the directory where your binary mask images are stored
image_directory = "C:\\Users\\Manoj\\Desktop\\b"

# Load the reference binary map image
reference_image_path = "C:\\Users\\Manoj\\Desktop\\nrsc\\binary_map.TIFF"
reference_image = io.imread(reference_image_path)

# Convert reference_image to grayscale if it's not already
if reference_image.ndim == 3:
    reference_image = color.rgb2gray(reference_image)

# Create an empty list to store results
results = []

# Iterate through each composite image
composite_directory = "C:\\Users\\Manoj\\Desktop\\output_binary_maps"
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

for month in months:
    composite_image_path = os.path.join(composite_directory, f"{month}_composite_binary_map.TIFF")
    composite_image = io.imread(composite_image_path)

    # Convert composite_image to grayscale if it's not already
    if composite_image.ndim == 3:
        composite_image = color.rgb2gray(composite_image)

    # Iterate through each image in the directory
    for filename in os.listdir(image_directory):
        if filename.endswith(".TIFF"):  # Adjust the file extension as needed
            image_path = os.path.join(image_directory, filename)

            # Load the target binary mask image
            target_image = io.imread(image_path)

            # Convert target_image to grayscale if it's not already
            if target_image.ndim == 3:
                target_image = color.rgb2gray(target_image)

            # Calculate SSIM (Structural Similarity Index)
            ssim_value = metrics.structural_similarity(composite_image, target_image)

            # Calculate MSE (Mean Squared Error)
            mse_value = metrics.mean_squared_error(composite_image, target_image)

            # Store the results as a tuple (composite_image, filename, SSIM, MSE)
            results.append((f"{month}_composite_binary_map.TIFF", filename, ssim_value, mse_value))

# Print the results
for composite_filename, target_filename, ssim_value, mse_value in results:
    print(f"Composite Image: {composite_filename}, Target Image: {target_filename}, SSIM = {ssim_value:.4f}, MSE = {mse_value:.4f}")


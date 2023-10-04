import os
import numpy as np
from skimage import io

# Function to load and process a single image
def process_image(image_path, weights):
    try:
        mask = np.array(io.imread(image_path))
    except FileNotFoundError:
        print(f"Image not found for {image_path}. Skipping...")
        return None
    year = int(os.path.basename(image_path).split('_')[1][:4])  # Extract the year from the filename
    weighted_mask = mask * weights[year]
    return weighted_mask

def main():
    # Input the directory where your binary mask images are stored
    root_directory = input("Enter the path to the directory where binary mask images are stored: ")

    # Input the start and end years
    start_year = int(input("Enter the start year: "))
    end_year = int(input("Enter the end year: "))

    # Input the output path for the binary map TIFF image
    output_binary_map_path = input("Enter the path to save the binary map as a TIFF image: ")

    # Define the weights for each year based on user input
    weights = {year: year - start_year + 1 for year in range(start_year, end_year + 1)}

    # Initialize an empty array for the final weighted sum result
    weighted_sum = None

    for year in range(start_year, end_year + 1):
        for month in months:
            # Construct the filename for each month and year
            filename = f"{month}{year}_mask.TIFF"  # Adjust the file extension as needed
            image_path = os.path.join(root_directory, filename)

            # Process the image and accumulate the weighted sum
            weighted_mask = process_image(image_path, weights)
            if weighted_mask is not None:
                if weighted_sum is None:
                    weighted_sum = weighted_mask
                else:
                    weighted_sum += weighted_mask

    # Calculate the threshold value as the sum of weighted values of the last 13 years (2011 to 2023)
    last_13_years_weights = [weights[year] for year in range(end_year - 12, end_year + 1)]
    threshold_value = sum(last_13_years_weights)

    # Create a boolean array where True represents a cloudy area and False represents a cloud-free area
    cloudy_area = weighted_sum <= threshold_value

    binary_map = np.zeros_like(weighted_sum)

    # Set the pixels classified as cloud-free to 1
    binary_map[~cloudy_area] = 255

    # Print the binary map
    print(binary_map)

    # Save the binary map as a TIFF image
    io.imsave(output_binary_map_path, binary_map)

    print(f"Binary map saved to {output_binary_map_path}")

if __name__ == "__main__":
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    main()

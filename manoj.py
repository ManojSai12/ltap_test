import numpy as np
import tifffile as tiff

# List of file paths to the 12 TIFF images
image_paths = [
    "apr2000_mask.TIFF",
    "apr2001_mask.TIFF",
    "apr2002_mask.TIFF",
    "apr2003_mask.TIFF",
    "apr2004_mask.TIFF",
    "apr2005_mask.TIFF",
    "apr2006_mask.TIFF",
    "apr2007_mask.TIFF",
    "apr2008_mask.TIFF",
    "apr2009_mask.TIFF",
    "apr_2010_mask.TIFF",
    "apr_2011_mask.TIFF",
    "apr_2012_"

    # Add paths to the remaining images here
]

# Initialize an array to store the composite image
composite_image = None

for image_path in image_paths:
    # Load the TIFF image
    image = tiff.imread(image_path)

    # Initialize or combine the images to create the composite
    if composite_image is None:
        composite_image = image
    else:
        # Perform the compositing operation (e.g., addition or blending)
        composite_image += image  # Change this operation as needed

# Save the composite image as a TIFF file
tiff.imsave("composite_image.TIFF", composite_image)

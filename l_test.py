import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Load the image (replace 'image_path' with your image path)
image_path = "C:\\Users\\Manoj\\Desktop\\b\\aug_binary_map.TIFF"
image = io.imread(image_path)

# Create a histogram of pixel values
hist, bins = np.histogram(image, bins=256, range=(0, 256))

# Plot the histogram
plt.plot(hist, color="black")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

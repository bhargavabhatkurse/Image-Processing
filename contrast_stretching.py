
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def contrast_stretching(image): 
	# Calculate minimum and maximum pixel intensities
    min_val = np.min(image)
    max_val = np.max(image)
    print(min_val,max_val)
    
    # Perform contrast stretching(min-max stretching)
    stretched_image = (image - min_val) * (255.0 / (max_val - min_val))
    
    # Convert the image back to uint8 data type
    stretched_image = stretched_image.astype(np.uint8)
    
    return stretched_image



# Load the RGB image
img_rgb = cv.imread('original/low_contrast.jpg')
transformed = contrast_stretching(img_rgb)

# Display the grayscale image
cv.imshow("original",img_rgb)
cv.imshow('stretched', transformed)
cv.waitKey(0)


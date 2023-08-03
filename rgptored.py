import cv2

# Load the RGB image
rgb_image = cv2.imread('original/2.jpg')

# Split the image into its red, green, and blue channels
b, g, r = cv2.split(rgb_image)

# Set the green and blue channels to zero
g[:] = 0
b[:] = 0

# Merge the red channel back into an RGB image
red_image = cv2.merge([b, g, r])

# Save the red image
cv2.imwrite("2.jpg", red_image)

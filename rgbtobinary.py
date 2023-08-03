# import required libraries
import cv2

# Load the RGB image
img = cv2.imread("original/4.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('4.jpg', binary)
cv2.waitKey(0)
cv2.imwrite("4.jpg", binary)
cv2.destroyAllWindows()
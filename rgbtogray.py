
import cv2

# Load the RGB image
img_rgb = cv2.imread('original/1.jpg')

# Convert the image to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Display the grayscale image
cv2.imshow('D:1.jpg', img_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite("1.jpg", img_gray)

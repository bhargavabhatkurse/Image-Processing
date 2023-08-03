
import cv2 as cv
import matplotlib.pyplot as plt

def rescaleFrame(frame,scale):
	#images, videos, live video
	width = int(frame.shape[1] * scale) #converting floating point to integer
	height = int(frame.shape[0] * scale)

	dimension = (width,height)
	# print(frame.shape[1],frame.shape[0])
	# print(dimension)

	return cv.resize(frame,dimension,interpolation = cv.INTER_AREA) #for scaling down

# Load the RGB image
img_rgb = cv.imread('original/2.jpg')

rescaled = rescaleFrame(img_rgb,0.40)

# Display the grayscale image
cv.imshow("original",img_rgb)
cv.imshow('scaled', rescaled)
cv.waitKey(0)


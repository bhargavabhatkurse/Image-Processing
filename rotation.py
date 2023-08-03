
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def transformation(frame): 
 	##channels is the number of color channels in the image
	rows, cols, channels = frame.shape
 	
 	#mapping 3 points to the corresponding outputs
 	# 						   (center, angle, scale)
	M = cv.getRotationMatrix2D((rows/2, cols/2), -30, 0.5)
	dst = cv.warpAffine(frame, M, (cols, rows))

	return dst

# Load the RGB image
img_rgb = cv.imread('original/3.jpg')
transformed = transformation(img_rgb)

# Display the grayscale image
cv.imshow("original",img_rgb)
cv.imshow('transformed', transformed)
cv.waitKey(0)


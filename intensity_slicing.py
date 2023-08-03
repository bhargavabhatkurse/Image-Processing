
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def slicing(frame): 
	r,c,ch = frame.shape
	img_thresh_back = np.zeros((r,c), dtype = int)
	lower_thresh = 100
	upper_thresh = 200
	highlight_value = 150

	if len(frame.shape) > 2:
 		image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	result = image.copy()
 	
	for i in range(r):
		for j in range(c):  
			if (lower_thresh < result[i,j]) and (result[i,j] < upper_thresh):  
				result[i,j]= 255
			else:
				result[i,j] = 0


	return result

# Load the RGB image
img_rgb = cv.imread('original/2.jpg')
transformed = slicing(img_rgb)

# Display the grayscale image
cv.imshow("original",img_rgb)
cv.imshow('slicing', transformed)
cv.waitKey(0)


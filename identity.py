
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def transformation(frame): 
	
	rows, cols, ch = frame.shape
 	
 	#mapping 3 points to the corresponding outputs
	pts1 = np.float32([[0, 0],			
                   	   [1, 0],
                   	   [0, 1]])
 
	pts2 = np.float32([[0, 0],			
                       [1, 0],
                   	   [0, 1]])
 
	M = cv.getAffineTransform(pts1, pts2)
	dst = cv.warpAffine(frame, M, (cols, rows))

	return dst

# Load the RGB image
img_rgb = cv.imread('original/1.jpg')
transformed = transformation(img_rgb)

# Display the grayscale image
cv.imshow("original",img_rgb)
cv.imshow('transformed', transformed)
cv.waitKey(0)


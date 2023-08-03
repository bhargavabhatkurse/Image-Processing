
import cv2

normal = cv2.imread('original/3.jpg')
gray = cv2.cvtColor(normal, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)
cv2.waitKey(0)

normal_again = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

#normal again is made green
normal_again[:, :, 0] = 0
normal_again[:, :, 2] = 0

cv2.imshow('image',normal_again) #green image
cv2.waitKey(0)

cv2.imwrite("3.jpg", normal_again)



import cv2 as cv
import numpy as np

def slicing(image): 
    bit_planes = []
    for i in range(8):
        #bitwise and of the ith bit of image with ith power of 2
        # this way we can extract the ith bit
        bit = np.bitwise_and(image, 2**i)  # Extract the i-th bit plane
        bit_planes.append(bit)

# Display the bit planes
    for i, bit in enumerate(bit_planes):
        cv.imshow(f'Bit Plane {i}', bit)
        cv.waitKey(0)
        cv.destroyAllWindows()

    result = np.zeros_like(bit_planes[0])   #same shape and dimension as the original one

    for i, bit_plane in enumerate(bit_planes):
        bitmask = 2**i
        result = np.bitwise_or(result, bitmask * bit_plane)

    result = (result * 255.0 / np.max(result)).astype(np.uint8)

    return result

# Load the RGB image
img_rgb = cv.imread('original/4.jpg')
gray = cv.cvtColor(img_rgb,cv.COLOR_BGR2GRAY)
cv.imshow("original",gray)
cv.waitKey(0)
transformed = slicing(gray)
cv.imshow("recreated: ",transformed)
cv.waitKey(0)



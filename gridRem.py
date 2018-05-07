import cv2
import numpy as np

img = cv2.imread('input.png')
# edges = cv2.Canny(img,100,110)

# masked_data = cv2.bitwise_and(img, img, mask=edges)
kernel = np.ones((10,10),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(img,kernel,iterations = 1)
# inpain = cv2.inpaint(img,masked_data,10,cv2.INPAINT_NS)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# erosion = cv2.erode(img,kernel,iterations = 1)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# cv2.imwrite('./mayo/closing.png',closing)
cv2.imwrite('output.png',dilation)

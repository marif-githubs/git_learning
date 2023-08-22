
import cv2
import numpy as np

print("package imported")
img=cv2.imread("C:\Users\Dell\OneDrive\Desktop\id photo.jpg")
cv2.imshow("marif",img)
##nigga
##nigga
print(img.shape)
resizeimg=cv2.resize(img,(1000,500))
print(resizeimg.shape)
cv2.imshow("output",resizeimg)
cv2.waitKey(50000)

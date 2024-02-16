import cv2
import numpy as np

#read an image

img = cv2.imread("imge/fruits.jpg")

# print(type(img))
# print(img.shape)

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img_resize= cv2.resize(img,(252,252))

# img_flip = cv2.flip(img,-1)

# img_crop = img[0:200, 0:200]

# cv2.imwrite('fruits_small.png', img_crop)

# # imgBlue = img[:,:,0]
# # imgGreen = img[:,:,1]
# # imgRed = img[:,:,2]

# # new_img = np.hstack((imgBlue, imgGreen, imgRed))

# cv2.imshow("window", img_crop)
# cv2.waitKey(0)

# print(img_resize.shape)

img= np.zeros((512,512,3))

cv2.rectangle(img, pt1= (100,100), pt2=(300,300), color=(0,255,0), thickness=-3)
cv2.circle(img, center=(100,400), radius=50, color=(255,0,0), thickness=-1)
cv2.line(img, pt1=(0,0), pt2=(512,512), thickness=3, color=(0,0,255))
cv2.putText(img, org=(200,400), fontScale=4, color= (0,255,255),thickness=2, lineType=cv2.LINE_AA, text="hy", fontFace=cv2.FONT_HERSHEY_PLAIN)

cv2.imshow('window', img)
cv2.waitKey(0)
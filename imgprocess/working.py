import cv2
import numpy as np

drawing= False
ix = -1
iy = -1

def draw(event, x, y, flags, params):

    global drawing,ix,iy

    if event == 1:
        drawing = True
        ix=x
        iy=y

    elif event == 0:
        if drawing == True:
          cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y),color= (0,0,255), thickness=-1)

    elif event == 4:
        drawing = False
        cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y),color= (0,0,255), thickness=-1)



    # print("event triggered")
    # print("event")

    # if event == 0:
    #     print("mouse moved")

    # if event == 1:
    #     print("mouse down clicked")

    # if event == 4:
    #     print("mouse up clicked")

    # if event == 1:
    #     cv2.circle(img, center=(x,y), radius=50, color=(255,0,0), thickness=-1)
    


    

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', draw)

img=np.zeros((512,512,3))

while True:

    cv2.imshow('window', img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
import cv2
import numpy as np
mode = True
drawing = False
ix,iy = -1,-1


#raw black background image
img = np.zeros((1080,1920,3),np.uint8)
cv2.namedWindow('image')
#mouse tracking function
def draw_circle(event,x,y,flags,param):
    global mode,drawing,ix,iy,r,g,b,radius

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            else:
                cv2.circle(img,(x,y),radius,(b,g,r),-1)

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv2.circle(img,(x,y),radius,(b,g,r),-1)
#nothing function for trackbar
def nothing(x):
    pass

#filling the selected color into the color selector viewer
#creating trackbar
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('radius','image',0,100,nothing)



def draw_rectangle(r,g,b):
    cv2.putText(img,'Selected color',(200,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
    cv2.rectangle(img,(0,0),(200,100),(b,g,r),-1)

cv2.setMouseCallback('image',draw_circle)

#main function
while(1):
    cv2.imshow('image',img)
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    radius = cv2.getTrackbarPos('radius','image')
    
    draw_rectangle(r,g,b)
    
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k==27:
        break
cv2.destroyAllWindows()

import cv2
import numpy as np
import imutils
cam=cv2.VideoCapture(0)
rw=3.26#reference object width (in inches)
rh=2.26 #reference object height (in inches)
pw=136
ph=93
rl=10.62 #distance of camera from reference (in inches)
l=float(input("Enter the distance of camera from reference (in inches):"))
f1=round(((rl*pw)/rw),3)
c1=round((l/f1),3)#pixel_to_metric_ratio of width
f2=round(((rl*ph)/rh),3)
c2=round((l/f2),3)#pixel_to_metric_ratio of height
while True:
        ret,image = cam.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        edged = cv2.Canny(gray, 50, 100)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c=max(cnts,key=cv2.contourArea)
        marker=cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        (x,y,w,h)=cv2.boundingRect(c)
        w=round(w*c1,3)
        h=round(h*c2,3)
        cv2.putText(image,"dims={}x{} inches".format(w,h),(x,y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1)	
        cv2.imshow("output",image)
        if cv2.waitKey(20)==ord('q'):
            break
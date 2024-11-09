import cv2
import numpy as np 
import sys
sys.path.append("E:\Lib\sites\mediapipe")
import mediapipe as mp
import HandTrackingModule as htm 
import math
import pyautogui  





webcam = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.7)
sw, sh = pyautogui.size() 
#print("the width of the screen is:",sw) the width of the screen
#print("the height of the screen is:",sh) the height of the scrren
print(webcam)




while True:
    ret,img = webcam.read()
    wcam = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    hcam = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    img = detector.findHands(img , draw=True)
    lmlist = detector.findPosition(img)
    #print(lmlist)
    if len(lmlist)!=0:
        print(lmlist[4],lmlist[8])
        
        x1 , y1 = lmlist[4][1] , lmlist[4][2]
        x2,y2  = lmlist[8][1] , lmlist[8][2]
        x3,y3 = lmlist[12][1] , lmlist[12][2]
        x4,y4 = lmlist[16][1] , lmlist[16][2]
        x5,y5 = lmlist[20][1] , lmlist[20][2]
        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x3,y3),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x4,y4),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x5,y5),15,(255,0,255),cv2.FILLED)
        
        length = math.hypot(x2-x1,y2-y1)
        #print(length)
        fingers = detector.getFingers(img)
        if fingers[1]==1 and fingers[2]==0:
            cv2.circle(img,(x2,y2),15,(66,135,245),cv2.FILLED)
            x6 = np.interp(x2,(0,wcam),(0,sw))
            y6 = np.interp(y2,(0,hcam),(0,sh))
            pyautogui.moveTo(sw-x6,y6)
        elif fingers[1]==1 and fingers[2]==1:
            pyautogui.click()
            
                
            
            
            
           
            
            
        
        
            
        
        
    cv2.imshow("frame",img)
    k = cv2.waitKey(13)
    if k == ord('s'):
        break
    
webcam.release()
cv2.destroyAllWindows()

    
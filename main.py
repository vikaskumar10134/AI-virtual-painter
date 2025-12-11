import time
import cv2
import mediapipe as mp
import os
import numpy as np
import hand_track_module as htm

brushThickness = 15
EraserThickness = 80

folderPath = r'D:\Data Science\Real time library\Mediapipe\08-Ai virtual painter\header'

myList = os.listdir(folderPath)

# print(myList)
OverlayList = []

# To read the images
for imPath in myList:

    # read the image
    image = cv2.imread(f'{folderPath}/{imPath}')

    OverlayList.append(image)

print(len(OverlayList))


header = OverlayList[0]
drawColor = (255 , 0 , 255)

# open the webcam and set height and width
cap = cv2.VideoCapture(0)
cap.set(3 , 1280)
cap.set(4 , 720)

previous_time = 0

# make object for detect the hand
detector = htm.HandDector(min_detection_confidence = 0.50)
xp , yp = 0 , 0

imagCanvas = np.zeros((720 , 1280 , 3) , np.uint8)

while True:

    # 1. import the images
    succes , frame = cap.read()

    # if some error occured and not read
    if not succes:
        break

    # flip the image
    frame = cv2.flip(frame , 1)

    # 2 . find hand landmark
    frame = detector.findHands(frame)

    # to find the landmark list
    landmark_list = detector.findPosition(frame , draw = False)

    if len(landmark_list) != 0:

        #print(landmark_list)

        # tip of index and middle finger
        x1 , y1 = landmark_list[8][1:]
        x2 , y2 = landmark_list[12][1:]



        # 3. Check which finger are up
        fingers = detector.fingersUp()

        #print(fingers)

        # 4. If selection mode --> Two finger are up
        if fingers[1] and fingers[2]:

            xp , yp = 0 , 0
            

            if y1 < 125:

                if 250 < x1 < 450:

                    header = OverlayList[0]
                    drawColor = (255 , 0 , 255)


                elif 550 < x1 < 750:

                    header = OverlayList[1]
                    drawColor = (255 , 0 , 0)

                elif 800 < x1 < 950:

                    header = OverlayList[2]
                    drawColor = (0 , 255 , 0)

                elif 1050 < x1 < 1200:

                    header = OverlayList[3]
                    drawColor = (0 , 0 , 0)

            cv2.rectangle(frame , (x1 , y1-25) , (x2 , y2+25) , drawColor , cv2.FILLED)


        # 5. If drawing mode --> Index finger is up
        if fingers[1] and fingers[2] == False:


            cv2.circle(frame , (x1 , y1) , 15 , drawColor , cv2.FILLED)

            # if draw at first time
            if xp == 0 and yp == 0:

                xp , yp = x1 , y1

            # for erasing
            if drawColor == (0 , 0 , 0):

                cv2.line(frame , (xp , yp) , (x1 , y1) , (drawColor) , EraserThickness)
                cv2.line(imagCanvas , (xp , yp) , (x1 , y1) , (drawColor) , EraserThickness)


            # otherwise drawing
            else:
                cv2.line(frame , (xp , yp) , (x1 , y1) , (drawColor) , brushThickness)
                cv2.line(imagCanvas , (xp , yp) , (x1 , y1) , (drawColor) , brushThickness)

            xp , yp = x1 , y1   # update the point

            

    imgGray = cv2.cvtColor(imagCanvas , cv2.COLOR_BGR2GRAY)

    _ , imgInv = cv2.threshold(imgGray , 50 , 255 , cv2.THRESH_BINARY_INV)

    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame , imgInv)
    frame = cv2.bitwise_or(frame , imagCanvas)


    # setting the header image
    frame[0:125 , 0:1280 , :] = header

    

    #frame = cv2.addWeighted(frame , 0.5 , imagCanvas , 0.5 , 0)

    # show the fps
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time


    # show on frame 
    cv2.putText(frame , f'FPS : {int(fps)}' , (70 , 70) , cv2.FONT_HERSHEY_PLAIN , 2 , (255 , 255 ,0) , 2)


    # to show the frame
    cv2.imshow('frame ' , frame)
    #cv2.imshow('Canvas ' , imagCanvas)

    # user press q it break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):

        print('Quiting....')
        break

cap.release()
cv2.destroyAllWindows()
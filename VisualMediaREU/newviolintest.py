import cv2
import numpy as np
# import keyboard


cap = cv2.VideoCapture('moreviolinimage.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
vidObj = cv2.VideoCapture('moreviolinimage.mp4')
frame = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

# while (fc < frameCount  and ret):
#     ret, frame[fc] = cap.read()
#     fc += 1

# print(frameCount)

# cap.release()
success = 1
i = -1
while success:
    i = i + 1
    value = input("Please enter a string:\n")
 
    print(f'You entered {value}')
    success, frame = vidObj.read()
    cv2.namedWindow('frame ' + str(i+1))
    cv2.imshow('frame ' + str(i+1), frame)
    cv2.waitKey(0)

    if value=='q':
        #print(0xff)
        folder = 'notPlaying'
    if value=='w':
        #print(0xff)

        folder = 'bowPlaying'
    if value=='e':
        folder = 'colLegno'
    if value=='r':
        folder = 'pizz'
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('rawData/'+ folder + '/newFrame'+str(i)+'.jpg', frame)
    print('frame done')
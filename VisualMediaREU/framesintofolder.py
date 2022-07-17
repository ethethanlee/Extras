import cv2
 
# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture('violin.mp4')
i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
    
    cv2.namedWindow('frame ' + str(i+1))
    cv2.imshow('frame ' + str(i+1), frame[i])
    if cv2.waitKey(0) & 0xff == ord('q'):
        folder = 'notPlaying'
    if cv2.waitKey(0) & 0xff == ord('w'):
        folder = 'bowPlaying'
    if cv2.waitKey(0) & 0xff == ord('q'):
        folder = 'colLegno'
    if cv2.waitKey(0) & 0xff == ord('q'):
        folder = 'pizz'
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('/Users/ethanlee/Developer/Extras/VisualMediaREU/' + folder + 'Frame'+str(i)+'.jpg', frame)
    i += 1
 
cap.release()
cv2.destroyAllWindows()
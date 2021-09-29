import cv2

camera = "http://192.168.43.163:8080/video"
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(camera)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(r"wv\IP_Camera.avi", fourcc, 30.0, (720,480))

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret==True:
        frame = cv2.resize(frame, (720,480))
        cv2.imshow("Mobile Camera",frame)
        output.write(frame)
        
        if cv2.waitKey(1)==ord("q"):
            break
        
cap.release()
output.release()
cv2.destroyAllWindows()
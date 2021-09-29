import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = "http://192.168.43.163:8080/video"
cap.open(camera)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(r"wv\test.avi", fourcc, 30.0, (720, 480), 0)

while True:
    ret,frame = cap.read()
    
    if ret == True:
        frame = cv2.resize(frame, (720, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("Camera Capture", frame)
        cv2.imshow(" gray Camera Capture", gray)
        output.write(gray)
        
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
output.release()
cv2.destroyAllWindows()
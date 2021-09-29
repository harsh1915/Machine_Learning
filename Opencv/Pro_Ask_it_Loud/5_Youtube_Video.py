import cv2

import pafy
url = "https://youtu.be/2UaVsc5Zjk4"
data = pafy.new(url)
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.open(data.url)

while True:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (720, 480))
        cv2.imshow("YouTube Video", frame)
        if cv2.waitKey(30) == ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()
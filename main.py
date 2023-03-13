import cv2
import numpy as np

vid = cv2.VideoCapture("reyon.mp4")
backsub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640,480))
    if ret:
        fgmask = backsub.apply(frame)


        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        try:
            hierarchy = hierarchy[0]
        except:
            hierarchy = []
        c = 0
        for contour, hier in zip(contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contour)
            if w > 60 and h > 100:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

                c += 1

        cv2.putText(frame, "insan: " + str(c), (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("insan sayisi", frame)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()

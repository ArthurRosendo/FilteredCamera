import cv2
import numpy as np

video_path = "a.mp4"
cap = cv2.VideoCapture(video_path)
#cap = cv2.VideoCapture(0)
if (cap is None) or (not cap.isOpened()):
    print("Invalid camera or video path")
    quit()
cv2.namedWindow("WebCam", cv2.WINDOW_FREERATIO)

#cap.set(cv2.CAP_PROP_POS_FRAMES, 2000) # TODO: remove, just for test

while True:
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('q'):
        break

    # The 255 part of the eps argument is necessary since we are working with 8-bits per channel, but the original paper on guided filters used a 0.0 to 1.0 range.
    frame = cv2.ximgproc.guidedFilter(frame, frame, 8, pow((0.4*255), 2), frame)
    cv2.imshow('WebCam', frame)

cap.release()
cv2.destroyAllWindows()

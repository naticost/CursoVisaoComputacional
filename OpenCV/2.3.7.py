import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_referencia = None

while True:
    ret,frame = cap.read()

    if frame_referencia is None:
        frame_referencia = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        continue
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(frame_referencia, frame_gray)

    _, thresholded = cv2.threshold(diff, 60,255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE,kernel)

    cv2.imshow('Original', frame)
    cv2.imshow('Diferença', diff)
    cv2.imshow('Limiarização', thresholded)

    key = cv2.waitKey(1)

    if key == ord('e'):
        frame_referencia = frame_gray

    elif key == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
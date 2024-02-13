import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    output = cv2.hconcat([gray, equalized])

    cv2.imshow('Webcam + Equalizador', output)

    if cv2.waitKey(1) == 29:
        break

cap.realease()
cv2.destroyAllWindows()
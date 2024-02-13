import cv2 as cv
import pytesseract as pyt

webcam = cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    _, frame = webcam.read()
    d = pyt.image_to_data(frame, output_type=pyt.Output.DICT)

    for i in range(len(d['text'])):
        x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
        if d['text'][i] == 'PASS' :
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        if d['text'][i] == 'FAIL':
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

    cv.imshow('Frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
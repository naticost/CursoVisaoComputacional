from flask import Flask, request
import cv2 as cv
import base64

app = Flask('Web')
webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

@app.route('/imagem', methods=['POST', 'GET'])
def imagem():
    try:
        while True:
            img = webcam.read()[1]
            ret, buffer = cv.imencode('.jpg',img)
            buffer64 = base64.b64encode(buffer)
            string64 = buffer64.decode('ascii')
            string = "data:image/jpg;base64," + string64
            imghtml = f'<img src="{string}">'
            return imghtml
    except Exception as e:
        return {'erro': f'{e}'}, 400
    
@app.route('/img', methods=['POST', 'GET'])
def abrir_Camera():
    try:
        while True:
            img = webcam.read()[1]
            ret, buffer = cv.imencode('.jpg', img)
            buffer64 = base64.b64encode(buffer)
            string64 = buffer64.decode('ascii')
            string = "data:image/jpg;base64," + string64
            imgDic = {'imagem': string}
            return imgDic
    except Exception as e:
        return {'erro':f'{e}'}, 400
app.run(host=('0.0.0.0'))
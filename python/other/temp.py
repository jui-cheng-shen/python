import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

cap = cv2.VideoCapture(0)


def putText(x, y, text, size=20, color=(0, 0, 0)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(fontpath, size)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)


def mosaic(image, level):
    size = image.shape
    h = int(size[0]/level)
    w = int(size[1]/level)
    output = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(
        output, (size[1], size[0]), interpolation=cv2.INTER_NEAREST)
    return output


qrcode = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (720, 420))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)

    if ok:
        for i in range(len(data)):
            text = data[i]

            if text == 'a1':
                img = cv2.blur(img, (20, 20))
                putText(0, 0, '模糊效果', 100, (255, 255, 255))

            elif text == 'a2':
                img = mosaic(img, 15)
                putText(0, 0, '馬賽克效果', 100, (255, 255, 255))

            elif text == 'a3':
                img = 255-img
                putText(0, 0, '負片效果', 100, (0, 0, 0))

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

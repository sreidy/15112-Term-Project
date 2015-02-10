# socure came from urllib documtation \
# extra help from  http://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera

import cv2
import urllib 
import numpy as np

androidPhone=urllib.urlopen('http://192.168.1.2:8080/videofeed')
bytes=''
while True:
    bytes+=androidPhone.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('super cool ipcam',i)
        if cv2.waitKey(1) ==27:
            exit(0)   
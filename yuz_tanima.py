import cv2
import os

# Kamera
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)
minW = 0.1 * camera.get(3)
minH = 0.1 * camera.get(4)

base_dir = os.path.dirname(os.path.abspath(__file__))

# Haarcascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# LBPH tanıyıcı
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(os.path.join(base_dir, "trainer.yml"))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im = camera.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
        _id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence < 50:
            # isim eşlemesi için labels dosyasını okuyabilirsiniz (istersen ekleyeyim)
            label = str(_id)
            conf_text = f"  {round(100 - confidence)}%"
        else:
            label = "unknown"
            conf_text = f"  {round(100 - confidence)}%"

        cv2.putText(im, label, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(im, conf_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', im)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
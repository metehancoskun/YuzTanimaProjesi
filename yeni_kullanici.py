import cv2
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))

# macOS için AVFoundation backend ile aç
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
camera.set(3, 640)
camera.set(4, 480)

# Kamera gerçekten açıldı mı kontrol et
if not camera.isOpened():
    print("Kamera açılamadı. macOS Kamera iznini kontrol edin (Sistem Ayarları > Güvenlik ve Gizlilik > Kamera).")
    print("Gerekirse PyCharm/Terminal uygulamasına izin verin ve başka bir uygulamanın kamerayı kullanmadığından emin olun.")
    sys.exit(1)

# İlk kareyi almayı deneyelim; donanım/izin kaynaklı sorunları erken yakalamak için
ret, test_frame = camera.read()
if not ret:
    print("Kameradan görüntü alınamadı. İzinleri ve kamera kullanımını kontrol edin.")
    camera.release()
    sys.exit(1)

# Haarcascade yolu
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# İlk test başarılıysa kullanıcı adını sor
name = input("Lütfen kullanıcı adınızı giriniz: ")

dirName = os.path.join(base_dir, "images", name)
print(dirName)
if not os.path.exists(dirName):
    os.makedirs(dirName)
    print("Klasör oluşturuldu")
else:
    print("İsim önceden kullanılmış")
    camera.release()
    sys.exit(0)

count = 1
while True:
    if count >= 100:
        break
    ret, im = camera.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        roiGray = gray[y:y + h, x:x + w]
        fileName = os.path.join(dirName, f"{name}{count}.jpg")
        cv2.imwrite(fileName, roiGray)
        cv2.imshow("face", roiGray)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
        count += 1

    cv2.imshow('im', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
# Yüz Tanıma Projesi

Bu proje, OpenCV kullanarak gerçek zamanlı yüz tanıma sistemi geliştirmek için oluşturulmuştur. LBPH (Local Binary Pattern Histogram) algoritması kullanılarak yüz tanıma işlemi gerçekleştirilir.

## Özellikler

- 📸 Kamera ile yeni kullanıcı kaydı
- 🎯 Yüz tespiti ve tanıma
- 📊 Eğitim verilerini işleme
- 🔍 Gerçek zamanlı yüz tanıma

## Gereksinimler

- Python 3.x
- OpenCV (cv2)
- NumPy
- PIL (Pillow)

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/YüzTanımaProjesi.git
cd YüzTanımaProjesi
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

### 1. Yeni Kullanıcı Ekleme

Yeni bir kullanıcı eklemek için `yeni_kullanici.py` dosyasını çalıştırın:

```bash
python yeni_kullanici.py
```

Program sizden kullanıcı adı isteyecek ve kameradan 100 adet yüz görüntüsü kaydedecektir.

### 2. Veri İşleme ve Eğitim

Kullanıcı görüntülerini işlemek ve modeli eğitmek için `veri_isleme.py` dosyasını çalıştırın:

```bash
python veri_isleme.py
```

Bu işlem `trainer.yml` ve `labels` dosyalarını oluşturur.

### 3. Yüz Tanıma

Gerçek zamanlı yüz tanıma için `yuz_tanima.py` dosyasını çalıştırın:

```bash
python yuz_tanima.py
```

Program kamerayı açacak ve tanıdığı yüzleri ekranda gösterecektir. Çıkmak için `ESC` tuşuna basın.

## Proje Yapısı

```
YüzTanımaProjesi/
├── Classifiers/
│   └── haarcascade_frontalface_default.xml
├── images/
│   └── [Kullanıcı Adları]/
│       └── [Görüntü Dosyaları]
├── veri_isleme.py      # Veri işleme ve model eğitimi
├── yeni_kullanici.py   # Yeni kullanıcı ekleme
├── yuz_tanima.py       # Yüz tanıma uygulaması
└── README.md
```

## Notlar

- macOS kullanıcıları için kamera izinlerini kontrol etmeyi unutmayın
- `trainer.yml` ve `labels` dosyaları otomatik oluşturulur ve `.gitignore` ile Git'e eklenmez
- Her kullanıcı için en az 50-100 görüntü önerilir

## Lisans

Bu proje eğitim amaçlıdır.


import pyqrcode

url = input("enter url to generate qr code: ") #dışarıdan giriş.

qr_code = pyqrcode.create(url) #import ettiğimiz pyqrcode ile create fonksiyonunun içine girilen url'yi yazarak qr kodu oluşturup değişkene atarız.
qr_code.svg('qrcode.svg',scale = 5) #svg cinsinden yazıyoruz. ismini ve ölçeğini yazdık.
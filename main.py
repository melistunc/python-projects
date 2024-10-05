
#1.yol (kod hata verdi)
#import pytube

#url = input("enter video url: ") #kullanıcı çalıştırdığında url gir diyecek.

#path = "" #path'ine boşluk verdik böylece dosyayı nerede çalıştırırsak kaydedeceğimiz videoyu direkt oraya kaydeder.

#pytube.YouTube(url).streams.get_highest_resolution().download(path)
#Youtube tanımlanmış bir sınıftır.pytube'u Youtube sınıfı içinde çalıştırırız.
#burası dışarıdan gelecek url'yi pytube fonksiyonuyla youtube sınıfı içinde streams ile çözünürlüğünü en yüksek yaparak alırız, download ile indiririz ve yeri de üstte tanımladığımız şekilde boş path olur.
#Python'da "streams", verilerin sırayla okunduğu veya yazıldığı, genellikle dosyalar, ağ bağlantıları veya cihazlar gibi kaynaklarla etkileşim sağlayan bir mekanizmadır.

#2.yol
import yt_dlp # YouTube'dan ve diğer video platformlarından video ve ses indirmeye yarayan bir Python modülüdür. Bu satırda yt_dlp modülü projeye dahil ediliyor.

url = input("enter video URL: ") #dışarıdan url değişkenine bir url girip atıyoruz.

path = ""  # Varsayılan olarak çalışma dizinine indirir. #path'ine boşluk verdik böylece dosyayı nerede çalıştırırsak kaydedeceğimiz videoyu direkt oraya kaydeder. Boş bırakılması, videonun programın çalıştığı dizine indirileceği anlamına gelir.

ydl_opts = { # Bu satır, yt_dlp modülüne indirmenin nasıl yapılacağına dair ayarları içeren bir sözlük (dictionary) oluşturuyor.

    'format': 'worst',  # En düşük çözünürlükte indirir.

    'outtmpl': path + '%(title)s.%(ext)s',  # outtmpl, indirilen dosyanın adını ve yolunu belirtir, %title%: İndirilen videonun başlığını kullanarak dosya adı oluşturur, %ext%: Dosyanın uzantısını (örneğin .mp4 veya .mkv) belirler, path + '%(title)s.%(ext)s': path değişkeniyle birlikte, videonun başlığı ve uzantısını kullanarak dosya yolu oluşturur. Eğer path boşsa, dosya çalışma dizinine indirilecektir.

}

try: #Bu blok, hataların kontrol edilmesi için kullanılır. Buradaki kod çalışırken hata oluşursa, except bloğuna geçilecek.

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: #yt_dlp.YoutubeDL() ile bir indirme yöneticisi (ydl) oluşturuluyor. ydl_opts sözlüğünde belirtilen ayarlar bu indirme yöneticisine aktarılıyor.
# with ifadesi, bu indirme yöneticisinin otomatik olarak açılmasını ve iş bittikten sonra kaynakların temizlenmesini sağlar.
        ydl.download([url]) #ydl.download() fonksiyonu, verilen URL’den videoyu indirir. Burada, kullanıcının girdiği URL'yi içeren bir liste oluşturularak indiriliyor.
#URL bir liste içinde verilmelidir, çünkü yt_dlp birden fazla videoyu da indirebilir.

    print("Download completed successfully.")

except Exception as e: #except bloğuna girer ve hata mesajını yakalar.

    print(f"An error occurred: {e}")


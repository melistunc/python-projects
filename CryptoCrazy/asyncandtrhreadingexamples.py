import threading
from http.client import responses
from threading import Thread
import requests
import time
import asyncio
import aiohttp
#Bu kod, belirtilen URL'lere eşzamanlı (synchronous) ve çoklu iş parçacığı (threading) kullanarak HTTP istekleri göndermekte ve işlem sürelerini karşılaştırmaktadır. İş parçacıkları sayesinde isteklerin paralel olarak işlenerek toplam sürenin azaltılması hedeflenmiştir.

#threading: Çoklu iş parçacığı oluşturmak için kullanılır.
#responses: HTTP yanıt kodlarının açıklamaları için içe aktarılmış ancak kullanılmamış.
#Thread: İş parçacığı başlatma sınıfı.threading.Thread sınıfını direkt kullanmayı sağlar.
#requests: HTTP isteklerini yapmak için kullanılır.
#time: İşlemlerin başlangıç ve bitiş zamanlarını kaydedip geçen süreyi ölçmek için kullanılır.


def get_data_sync(urls): #data için fonksiyon oluşturduk ve parametre olarak urls seçtik (urls gelen verileri alacak)
    st = time.time() #görev hangi zamanda çalışıyorsa o zamanı gösterir. işlem başlangıç zamanı st değişkenine kaydedilir.
    json_array = [] #gelen verilerin toplanacağı dizi. HTTP yanıtlarını saklamak için boş bir liste oluşturulur.
    for url in urls: #urls listesindeki her URL için sırayla requests.get() ile HTTP isteği gönderilir.
        json_array.append(requests.get(url).json()) #json dizisinin içine cevapları (url) get ile alıp json formatında yazıyoruz.Gelen yanıt json() ile JSON formatına çevrilip json_array listesine eklenir.

    et = time.time() #bitme zamanı
    elapsed_time = et - st #işlem bittiğinde geçen zamanı gösterir. kaç sn geçtiyse o saniyeyi verir.
    print("execution time: " ,elapsed_time, "seconds") #Geçen süre ekrana yazdırılır ve alınan JSON verileri döndürülür.
    return json_array #değişkeni json_array olarak döndürüyoruz.

class ThreadingDownloader(threading.Thread): #threading.Thread sınıfından türetilmiş bir özel sınıf oluşturulur.
    json_array = [] #İş parçacığı içinde gelen yanıtların saklanacağı bir json_array listesi tanımlanır.

    def __init__(self, url): #__init__ yöntemi ile sınıf başlatılır ve her iş parçacığı için bir url atanır. (__init__ metodu, Python'daki sınıflar için kurucu (constructor) işlevi görür. Bir sınıftan yeni bir nesne oluşturulduğunda, bu metot otomatik olarak çağrılır ve nesneyi başlatmak için kullanılır.)
      super().__init__() #super().__init__() ile threading.Thread'in başlangıç işlevselliği çağrılır.
      self.url = url

    def run(self):
        response = requests.get(self.url) #run() metodu, iş parçacığı çalıştırıldığında çağrılır ve belirtilen url'ye HTTP isteği gönderir.
        self.json_array.append(response.json()) #Gelen HTTP yanıtı JSON formatına çevrilip json_array listesine eklenir.
        print(self.json_array) #bununla da gelen data'ları görürüz. Gelen veriler ekrana yazdırılır ve liste olarak döndürülür.
        return self.json_array

def get_data_threading(urls):
        st = time.time()  # görev hangi zamanda çalışıyorsa o zamanı gösterir. İşlem başlangıç zamanı kaydedilir.
        threads = [] #İş parçacıklarını tutmak için boş bir threads listesi oluşturulur.
        for url in urls:
            t = ThreadingDownloader(url) #urls listesindeki her URL için bir ThreadingDownloader nesnesi oluşturulur.
            t.start() #İş parçacığı start() ile başlatılır ve threads listesine eklenir.
            threads.append(t)

        for t in threads: #İşlem sonunda geçen süre hesaplanır ve ekrana yazdırılır.
            t.join() #Her iş parçacığının tamamlanması için join() metodu çağrılır.
            #print(t) #data'nın gelip gelmediğini görmek için kullanırız.

        et = time.time()  # bitme zamanı
        elapsed_time = et - st  # işlem bittiğinde geçen zamanı gösterir. kaç sn geçtiyse o saniyeyi verir.
        print("execution time: ", elapsed_time, "seconds")





#İki farklı asenkron yaklaşım kullanarak, çok sayıda API isteğini verimli bir şekilde gerçekleştirmeyi hedefler.
#İlk yöntem tekil asenkron istekleri sırasıyla işler. İkinci yöntem ise eşzamanlı görevler oluşturup aynı anda çalıştırmayı dener.
#Ancak her iki yöntemde de bekleme süresi yüksek olduğu için işlem süreleri benzerdir.

async def get_data_async_but_as_wrapper(urls): #AA- bu kısım istediğimiz gibi çalışmadı. Bu bir asenkron fonksiyonu tanımlar.
    st = time.time()  # görev hangi zamanda çalışıyorsa o zamanı gösterir. İşlem başlangıç zamanı kaydedilir.
    json_array = [] #Yanıtların saklanacağı boş bir liste oluşturulur.

    async with aiohttp.ClientSession() as session: # Bir asenkron oturum başlatılır, bu oturum API'lere istek göndermek için kullanılır.
        for url in urls: #URL listesi üzerinde döngü başlatılır.
            async with session.get(url) as resp: #Her URL için bir GET isteği yapılır.
                json_array.append(await resp.json()) # Gelen yanıt JSON formatına çevrilip listeye eklenir.

    et = time.time()  # bitme zamanı
    elapsed_time = et - st  # işlem bittiğinde geçen zamanı gösterir. kaç sn geçtiyse o saniyeyi verir.İşlem süresi hesaplanır ve yazdırılır.
    print("execution time: ", elapsed_time, "seconds")
    return json_array # Toplanan JSON yanıtları döndürülür.


async def get_data(session, url, json_array): #Tek bir URL'den gelen veriyi JSON formatında alır ve listeye ekler.
    async with session.get(url) as resp: #GET isteği başlatılır.
        json_array.append(await resp.json()) #Yanıt JSON formatına dönüştürülüp listeye eklenir.


async def get_data_async_concurretly(urls): #AA- bu yüzden alternatif olarak bu kısmı yaparız.
    st = time.time()  # görev hangi zamanda çalışıyorsa o zamanı gösterir. İşlem başlangıç zamanı kaydedilir.
    json_array = [] # Yanıtların saklanacağı boş bir liste oluşturulur.

    async with aiohttp.ClientSession() as session: #Asenkron bir oturum başlatılır.
        tasks = [] #Asenkron görevleri saklamak için bir liste oluşturulur.
        for url in urls: #URL listesi üzerinde döngü başlatılır.
            tasks.append(asyncio.ensure_future(get_data(session,url,json_array))) # Her URL için bir görev oluşturulur ve görev listesine eklenir.
            await asyncio.gather(*tasks) #Tüm görevler eşzamanlı olarak çalıştırılır.

    et = time.time()  # bitme zamanı
    elapsed_time = et - st  # işlem bittiğinde geçen zamanı gösterir. kaç sn geçtiyse o saniyeyi verir.
    print("execution time: ", elapsed_time, "seconds")
    return json_array


urls = ["https://postman-echo.com/delay/3"] * 10 #10 kere b istek atılır ve bu istek 3 saniye sürer.
#get_data_sync(urls) #40 saniyede olmuştu threadsiz. Eşzamanlı veri alma fonksiyonu.

#get_data_threading(urls) #3 saniyede oluştu. Yani thread ile daha az sürede işleri yaparız.Çoklu iş parçacığıyla çalışan veri alma fonksiyonu.
#Kod, URL'lerden veri almak için iki yöntem sunar: eşzamanlı (tek seferde bir istek) ve çoklu iş parçacığı (aynı anda birden fazla istek). İş parçacığı yöntemi, paralel işleme sayesinde süreyi kısaltır ve daha verimli hale getirir.

#asyncio.run(get_data_async_but_as_wrapper(urls)) #42 saniye sürdü. İlk yöntem çalıştırılır.

asyncio.run(get_data_async_concurretly(urls)) #43 saniye sürdü.İkinci yöntem çalıştırılır. Görevler eşzamanlı yürütülerek işlem süresi kısaltılmaya çalışılır.
import requests

def get_crypto_data():
   response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
#veriyi alıp okumak istediğimizde genelde get kullanırız.
#genelde  bir şeyi yazacakken veritabanı değişikliği, backen'e bilgi yollamak için post kullanırız.
#delete veriyi silmek için kullanılan istek.
#puth veya patch veriyi güncellemek için kullanılan isteklerdir.

   if response.status_code == 200: #gelen cevabın kodu 200 ise
        return response.json() #bu datayı json olarak döndür

crypto_response = get_crypto_data() #fonksiyonu değişkene atadık.
user_input = input("Enter your criypto currency: ") #kullanıcıdan dışarıdan değer girmesini istedik.
x = 0 #sayaç için

for crypto in crypto_response: #crypto response'yi crypto içine atadık.
    if crypto["currency"] == user_input: #eğer kullanıcının girdiği input currency'e eşit ise
        print(crypto["price"]) #crypto'nun price'ını göster.
        break # loop devam etmesin bulduğunda çıksın diye kullanılır. Sonuçta o BTC'nin ka. dolar olduğunu gösterir.


    # print(response.status_code) # gelen cevabı ekrana yazdırdı

    #print(response.text) #cevabı bir metin olarak yazdırdı.

    #print(response.json()) #bir ürünün fiyatını görmek için vs kullanılabilir.

    #for crypto in response.json(): #json bir sözlük gibi çalışır. response json içindekileri crypto'ya atadık.
        #print(crypto["price"]) #crypto içinde price'ları listeledik.

import speech_recognition as sr
from speech_recognition import Microphone
from googletrans import Translator

#dışarıdan ses alımı
def speech_understand(): #yeni fonksiyon oluşturur.
    recognizer = sr.Recognizer()  # recognizer nesnesi oluşturuyoruz sr.Recognizer() sınıfı ile(sr içinden Recognizer adlı sınıf çağırdık bu sesin tanınmasını sağlar.). Dışarıdan gelen sesi kaydetmek için.
    with sr.Microphone() as source: #mikrofonu açıp otomatik kapanması için with kullandık ve mikrofonu açmak ve kaynak olarak kullanmak için sr sınıfı içinden Microphone metodunu çağırdık. Microphone dileme kaynağı olarak kullanılır. Mikrofonu açar.
        print("Speak Now: ")
        recognizer.adjust_for_ambient_noise(source)  # ortam gürültüsünü ayarlar.
        recognizer_talk = recognizer.listen(source) #recognizer nesnesini listen metoduyla çalıştırıp parametre olarak dışarıdan gelen kaynak(source)'u yazarak dışarıdan gelen sesin tanınmasını sağladık. recognizer.listen(source) ile kaydedilen ses verisini bir değişkene atadık çünkü mikrofonla kaydedilen sesi değil mikrofon kaynağını almalıyız ki çözümleyelim. Ses kaydını başlatır.

#hata mesajları
        try: #eğer sistem çalışırsa burası çalışacak.
            recognizer_text = recognizer.recognize_google(recognizer_talk, language="tr-TR")  # Kaydedilen sesi çözümlüyoruz. önce ses kaydediliyor ve ardından recognize_google() fonksiyonuna bu ses verisi iletiliyor.
            print(recognizer_text)
            return recognizer_text #çözümlenen metni döndürür.
        except sr.UnknownValueError: #sistem konuşmayı anlamazsa burası çalışacak.
            print("Dont understand. Speak again: ")
            return ""
        except sr.RequestError: #internet ağlarında sıkıntı varsa burası çalışacak.
            print("Please check your connection.")
            return ""

#dışarıdan alınan sesin çevrilmesi
def translate(recognizer_text): #translate adında bir fonksiyon tanımlanıyor. Bu fonksiyon, bir parametre alıyor, bu parametre daha önce konuşma tanıma işlemiyle elde edilen metni temsil ediyor (recognizer_text).
    translator = Translator() #Translator sınıfından bir nesne oluşturduk.Bu nesne google translate'i kullanarak çeviri işlemleri yapmamızı sağlar.
    result = translator.translate(recognizer_text, dest='en') #translator nesnesinin translate metodunu çağırıyoruz.recognizer_text parametresini alıp dest ile hedef dili ingilizce (en) yapıyoruz. result değişkeni çeviri sonucunu tutuyor. Bu kod metnin ingilizceye çevrileceğini açıklıyor.
    return result.text #bu çeviri metin içeriğini alır ve fonksiyonun çıktısı olarak geri döner.

if __name__ == "__main__": #burası python dosyasının doğrudan çalışıp çalışmadığını gösterir.
    recognizer_text = speech_understand()  # bu fonksiyon mikrofonla konuşmayı alır metne çevirir (speech_understand) ve recognizer_text değişkenine atar.
    if recognizer_text:  #eğer metin alındıysa (recognizer_text değişkeninin boş olup olmadığı kontrol edilir yani dışarıdan mikrofonla girdinin girilip girilmediği kontrol edilir.)
        last = translate(recognizer_text)  #çevirme işlemi yapılır.
        print(f"Çevirisi: {last}")  #çeviriyi yazdırır.










from tkinter import *
import os

#entry'yi doldurup (başlık için) enter'a basınca txt dosyası oluşturulur text kısmına metin girlip butına basıldıktan sonra şifrelenmiş metin kayıt edilir.

# Basit şifreleme fonksiyonu (Caesar Cipher)
def encrypt(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Sadece harfleri şifrele
            shift_base = 65 if char.isupper() else 97  # Büyük/küçük harf kontrolü
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Harf değilse olduğu gibi bırak
    return encrypted_text

# Entry'e girildiğinde girilen başlığa göre txt dosyası oluşturma
def create_file(event):
    global file_name  # file_name değişkenini global yap
    title = my_entry.get().strip()
    file_name = f"{title}.txt" if title else None

    # Dosya adını oluştur (başlık + .txt uzantısı)
    if file_name:
        try:
            # Boş bir dosya oluştur
            with open(file_name, "w") as file:
                pass  # İçerik yazmadan dosyayı açıp kapatır
            print(f"{file_name} dosyası oluşturuldu.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# Save & Encrypt butonuna basıldığında şifreleme işlemi ve dosyaya kaydetme
def save_and_encrypt():
    global file_name  # file_name değişkenine global olarak eriş
    secret_text = my_text.get("1.0", END).strip()
    encrypted_text = encrypt(secret_text)

    # Text alanından metni al
    secret_text = my_text.get("1.0", END).strip()  # Text alanının başlangıç ve bitiş konumu
    print(f"Girilen metin: {secret_text}")  # Girilen metni yazdır


    if file_name:  # Dosya adı varsa (daha önce oluşturulduysa)
        try:
            # Dosyaya şifrelenmiş metni yaz
            with open(file_name, "a") as file:  # Dosya modunu "a" (append) yaparak yazıyoruz
                file.write(encrypted_text)
            print(f"Şifrelenmiş metin {file_name} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    # Dosyanın nerede kaydedildiğini kontrol etmek
    current_dir = os.getcwd()
    print(f"Dosya şu dizinde oluşturuldu: {current_dir}/{file_name}")

# Başlangıçta file_name değişkenini None olarak tanımlıyoruz
file_name = None

#ekran oluşturmak
my_window = Tk()
my_window.title("Tkinter Python")
my_window.minsize(width=500, height=600)
my_window.config(padx=10, pady=10)

#foto ekleme, jpg resim yükleme
photo = PhotoImage(file= "topp.png")


#Resmi pencereye ekle
label_photo = Label(my_window, image=photo)
label_photo.pack()

#title
my_label = Label(text="Enter your title")
my_label.pack()

#entry
my_entry = Entry(width=30)
my_entry.pack()
my_entry.bind("<Return>", create_file) # "Enter" tuşuna basıldığında create_file fonksiyonu çağrılır

#title2
my2_label = Label(text="Enter your secret")
my2_label.pack()

#text
my_text = Text(width=30, height=10)
my_text.pack()

#1.buton
my_button = Button(text="Save & Encrypt", command=save_and_encrypt)
my_button.pack()


my_window.mainloop()
from cgitb import reset
from tkinter import *

#ekran oluşturuldu.
window = Tk()
window.title("Body Mass Index")
window.minsize(width=300, height=250)
window.config(padx=30, pady=30)

# kilo girişi yazı kısmı
label = Label(text="Enter Your Weight(kg)")
label.config(padx=10, pady=10)
label.pack()

# kilo girişi entry kısmı
entry = Entry(width=20)
entry.pack()

# boy girişi yazı kısmı
label2 = Label(text="Enter Your Height(cm)")
label2.config(padx=10, pady=10)
label2.pack()
# boy girişi entry kısmı
entry2 = Entry(width=20)
entry2.config()
entry2.pack()


#buton oluşturulması
def calculate_pack(): #kullanıcıdan alınan girişlerin(kilo ve boy) her zaman doğru formatta olmama ihtimalidir. Kullamıcı yanlışlıkla sayı yerine harf yazarsa program hata verir ve kapanır bu hataları önlemek için kullanırız.
    try: #kullanıcının verdiği verilerle BMI hesaplamasını dener. Eğer bu veriler geçerli ise (sayı formatında ise), işlem sorunsuz devam eder.
        weight = float(entry.get()) #kilo girişini al
        height = float(entry2.get()) / 100 #boy girişini al ve bunu metreye çevir.
        BMI = weight / (height ** 2) #BMI hesaplama
        if BMI < 16.0:
          result = f"Your BMI is {BMI:.2f}. You are severely underweight"
        elif 16.0 <= BMI < 18.5:
            result = f"Your BMI is {BMI:.2f}. You are underweight."
        elif 18.5 <= BMI < 25:
            result = f"Your BMI is {BMI:.2f}.You are normal weight."
        elif 25 <= BMI < 30:
            result = f"Your BMI is {BMI:.2f}.You are overweight."
        else:
            result = f"Your BMI is {BMI}:.2f. You are obese."

        result_label.config(text=result) #sonucu güncelle

    except ValueError: #kullanıcı yanlışlıkla geçersiz bir veri (örneğin harf, sembol, ya da boşluk) girerse işlemler hata verecektir. Bu hatayı ValueError yakalar ve kullanıcıya uygun bir uyarı mesajı gösterir, programın kapanmasını engeller.
        result_label.config(text="Please enter valid numbers!")

button = Button(text="Calculate", command = calculate_pack) #buton ile fonksiyonu birbirine bağladık.
button.config(padx=2, pady=2)
button.pack()

#sonuç gösteren etiket hata durumunu ekrana vermek için.
result_label = Label(text="")
result_label.pack()


window.mainloop()

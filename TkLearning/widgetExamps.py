from tkinter import * #bu şekilde yıldız dersek her şeyini import eder.

#ekranı oluşturduk.
my_window = Tk() #yıldız ile tüm her şeyi import ettiğmiz için her şeyi direkt alabilirizi.
my_window.title("Tkinter Python")
my_window.minsize(width=400, height=400)
my_window.config(padx=20, pady=20) #oluşturulan elemanların aralarına boşluk bırakır hem y düzleminden hem de x düzleminden boşluk bıraktı.


#yazı tarafını oluşturduk.
my_label = Label(text="my label")
my_label.config(bg="purple") #renk vs değiştirdik config ile.
my_label.config(fg="orange")
my_label.config(padx=10, pady=10) #label için boşluklar ayarladık. Label içinde ayar yaptı.
my_label.pack()


#buton oluşturuldu.
def mbutton_clicked(): #butona basıldığında kullanılacak fonksiyon.
    print("button clicked")
    print(my_text.get("1.0", END)) #text'te ne yazıldıysa ekrana bunu printler. Burada 1 ve END yazmak zorundayız çünkü text'i ekrana getireceksek onun nereden başlayıp nerede sonlanacağını yazmamız gerekiyor. 2'den de başlayıp farklı yerde sonlandırabilirdik. 1 hangi satırdan başladığı 0 ise hangi karakterden başlayacağını söyler.

my_button = Button(text="button", command=mbutton_clicked) #buton oluşturma nesnesi. text ile ismini command ile hangi fonksiyona göre çalışacağını belirttik.
my_button.config(padx=10, pady=10) #butonun y ve x olarak boşluklarını verdik.
my_button.pack()


#entry oluşturuldu. Kısa yazı yeri.
my_entry = Entry(width=20)
my_entry.pack()


#text kısmı oluşturuldu. Uzun yazı yeri. Birden fazla satır multiline
my_text = Text(width=30, height=10)
#my_text.focus() #yaparsak mouse otomatik olarak text'te gelir ve text'ten başlar.
my_text.pack()


#scale oluşturuldu, bir listeli düzen oluşturur.
def scale_selected(value): # listeyi kaydırınca ekrana sayıları yazması için oluşturduğumuz fonksiyon
    print(value) #fonksiyon value değeri alır çünkü basınca gelen tek değer değildir. Kaydırdıkça devamlı gelen bir listedir.
my_scale = Scale(from_=0, to=50, command=scale_selected) # 0'dan 50'ye kadar olan bir liste oluşturdu.
my_scale.pack()


#spinbox, kaydırmalı değil de akttan seçmeli listedir.
def spinbox_selected():
    print(my_spinbox.get()) #her seçimde ekrana yazdırır.
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected) # 0'dan 50'ye kadar oluşturdu.
my_spinbox.pack()


#checkbutton
def check_selected():
    print(checked_state.get()) #tıklandığında checkstate sayesinde tıklanınca 1, tıklanmayınca 0 verir.

checked_state = IntVar() #checkbutton seçildiyse 1 seçilmediyse 0 veren fonksiyon.
my_checkbutton = Checkbutton(text="check", variable=checked_state, command=check_selected) #burada check'in seçilip seçilmediğini görmek için bir variable vermemiz lazım. Vraiable hangisnin seçilip seçilmediğini kontrol eder.
my_checkbutton.pack()


#radio button, seçeneklerden bir tane tıklanması.
def radio_selected():
    print(radio_state.get()) #ekrana değerlerin getirlip görülmesi için

radio_state = IntVar() # seçimin yapılıp yapılmadığını görmek için
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_state, command=radio_selected) #value verilen değerdir.
my_radiobutton2 = Radiobutton(text="2.option", value=20, variable=radio_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton2.pack()


#listbox, bir listeyi kullanıcıya daha düzgün göstermeye yarıyor.
def listbox_selected(event): #liste içerisindeki elemanlara tıklandığında çalışır.
    print(my_listbox.get(my_listbox.curselection())) # o anda hangi eleman seçilmişse anlık olarak onu vermemizi sağlayan fonksiyondur (curselection)

my_listbox = Listbox()
name_list = ["mel", "abc", "kcs","hsk","kdjd"]
for i in range(len(name_list)):
    #print(i) #bu fonksiyon bize elemanların index numaralarını verir.
    my_listbox.insert(i, name_list[i]) #burası box'a listeyi yükler ve listeyi index numaralarına göre bize verir.

my_listbox.bind('<<ListboxSelect>>', listbox_selected) #listboxlarda, listbox'a fonksiyonu bu şekilde bağlarız. Kural gibidir.
my_listbox.pack()


my_window.mainloop()






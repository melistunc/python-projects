import tkinter

#window , ekran oluşturma.
window = tkinter.Tk() #window yani ekranı oluşturduk.
window.title("Python Tkinter") #ekran başlığı
window.minsize(width=300, height=300) #ekranın boyutunu ayarladık.


#buton için tanımladığımız fonksiyon burası butona basıldığında olacak şeydir.
def clicl_button():
    user_input = my_entry.get() #entry kısmına ne yazılırsa onu string olarak verir.
    print(user_input) #ekrana yazdırma



#label, metin(text) yerinin oluşturulması
my_label = tkinter.Label(text="this is a label") #içinde ne gösterilecek yazarız.
my_label.config( font=('Arial', 20, "italic")) #bu şekilde de düzenleme değişiklik yapabiliriz. Bu kısmı yukarıdaki satırla da yapabilirdik.
#my_label.pack() #mylabel'i ekranın ortalarında konumlandırmak için kullandığımız fonksiyondur.
#my_label.place(x=0, y=0) # bu label kısmını direkt nereye koyacağımızı soruyor. x ve y konumlarıyla burayı ayarlarız.
my_label.grid(row=2, column=1) # ekranı ızgaralara ayırırız grid ile. #row yatay satırlar, column dikey sütunlardır.



#button yapımı
my_button = tkinter.Button(text="this is a button", command=clicl_button) #buton ve text oluşturduk. command der ki biz bu butona basınca ne olsun onu belirleriz.
#my_button.pack() #pack gelen yerleşimleri gelen verileri alt alta koyuyor.
#my_button.place(x=100, y=150)
my_button.grid(row=1, column=1) #butona ızgara oluşturduk ve butonun yerini belirttik.



#entry, kullanıcıdan klavyesinden girdi aldırma yeri.
my_entry = tkinter.Entry(width=30) #dışarıdan alınacak girdi kısmı oluşturuldu. width onun boyutunu belirtir.
#my_entry.pack()
my_entry.grid(row=0, column=2) #entry için ızgaralar yaptık yerini yerleştirdik.



window.mainloop() #ekranın kapanmaması için kullanırız.
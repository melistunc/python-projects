import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("python turtle")
turtle.speed(0) #turtle hız arayını ayarlar. en hızlısı 0'dır.

turtle_instance = turtle.Turtle()


turtle_colors = ["red","purple","blue","green","orange","yellow"] #renk listesi

for i in range(20): # for ile loop oluştururuz bu da bize dairelerin alttan da üstten de iç içe daireler çizilmesini sağlar.
   turtle_instance.color(turtle_colors[i % 6]) #her seferinde renk değişsin. i % 6 demek i'nin 6 ile bölümünden kalanı bul onu da yaz. yani her seferinde sıfıdan 5'e kadar yazdırır. i 'ye istediğimiz değeri verebiliriz artık.
   turtle_instance.circle(10 * i) # daire şeklini çizdirme kodu.
   turtle_instance.circle(-10 * i) # eksi ılunca dönüş ekseni değişir.
   turtle_instance.left(i) #her döndüğünde kayarak gitsin.

turtle.mainloop() #done yerine bu da kullanılabilir. Aynı işlemlidir.
#turtle.done()

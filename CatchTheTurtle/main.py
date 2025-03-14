import turtle
import random
from os import write
from random import randint

#ekran ayarları
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("#006400")
turtle_screen.title("Catch The Turtle <3")

#turtle nesnesi oluşturma
my_turtle = turtle.Turtle() # turtle için kullanılan nesne tüm turtle ile ilgili kodlar bu turtle nesnesiyle yaılacak.
my_turtle.shape("turtle") # shape şekil demektir. İçine turtle yazark turtle resmi oluşturduk.
my_turtle.speed(0)

#ekran genişlik ve yükseklik sınırlarını alma.
screen_width = turtle_screen.window_width() / 2
screen_height = turtle_screen.window_height() / 2

game_over = False

#rastgele hareket fonksiyonu
def random_my_turtle():
   # turtle'ı rastgele bir açıdan döndür.
   my_turtle.penup() # oluşan çizgiyi siler.
   random_turtle = random.randint(0, 360)
   my_turtle.right(random_turtle)

   if game_over:
      return #oyun bittiyse hareket etmesin

   #turtle'ı rastgele bir mesafe ileri götür.
   random_turtle_two = random.randint(20, 100)
   my_turtle.forward(random_turtle_two)

   #turtle pozisyonunu kontrol et.
   x = my_turtle.xcor()
   y = my_turtle.ycor()

   #eğer sağ ve sol sınırı aşarsa geri döndür.
   if x > screen_width:
      my_turtle.setx(screen_width) #sınırda kalmasını sağla
      my_turtle.right(180) #geri dön

   elif x < -screen_width:
      my_turtle.setx(-screen_width) #sınırda kalmasını sağla
      my_turtle.right(180)

   #eğer üst veya alt sınırı aşarsa geri döndür.
   if y > screen_height:
      my_turtle.sety(screen_height) #sınırda kalmasını sağla
      my_turtle.right(180) #geri dön

   elif y < -screen_height:
      my_turtle.sety(-screen_height) #sınırda kalmasını sağla
      my_turtle.right(180)

   # 500 ms sonra tekrar hareket ettir.
   turtle_screen.ontimer(random_my_turtle, 500)

   return

#yazı nesnesi oluştur
score_show = turtle.Turtle()
score_show.penup()  #çizgi bırakmamak için kalemi kaldır
score_show.hideturtle()  #turtle'ı gizle
score_show.goto(0, 200)  #geri sayımı göstereceğin konum

#zamanlayıcı, geri sayım
def countdown(count): #sayaç fonksiyonu, count başlangıç değeri.

    if count > 0: #başlangıç değeri 0'dan büyükse.
       score_show.clear()  # eski sayıyı temizle. Her gelen yeni sayıyı güncellemek için.
       #yeni sayıyı yazdır.
       score_show.write(f"Time left: {count}", align="center", font=("Arial", 16, "normal"))
       #bir saniye sonra geri sayımı 1 azalt ve fonksiyonu tekar çağır.
       turtle_screen.ontimer(lambda: countdown(count - 1), 1000)

    else:
       global game_over
       game_over = True #game_over bayrağını aktif yap. Burası true olunca zaman doldu demek ve random_my_turtle ve tickle'daki fonksiyonlar bu bayrağı kontrol ediyor bununla oyunun bitip bitmediğini anlıyorlar. true olunca hareket ve puan artışı duruyor.
       score_show.clear()
       #zaman dolduğunda Oyun Bitti mesajını göster.
       score_show.write("Game Over!", align="center", font=("Arial", 16, "bold"))

countdown(30) #başlangıç değeri olarak 30 değerini verdik.


#puan değişkeni tanımı
score = 0

#yazı nesnesi oluştur
score_display = turtle.Turtle()
score_display.penup()  #çizgi bırakmamak için kalemi kaldır
score_display.hideturtle()  #turtle'ı gizle
score_display.goto(0, 260)  #puanı göstereceğin konum

#tıklama fonksiyonu, turtle koordinatları almak
def tickle(x, y):
   global score #global değişken. Çünkü score sonradan güncellenebilmeli.

   if game_over:
      return  # oyun bittiyse puan artmasın.

   #mevcut tıklama kontrolü
   turtle_x = my_turtle.xcor() #turtle'ın x koordinatı
   turtle_y = my_turtle.ycor() #turtle'ın y koordinatı

   #mesafe hesaplama
   distance =((x - turtle_x) ** 2 + (y - turtle_y) ** 2) ** 0.5

   #mesafe kontrolü
   if distance < 20: #mesafe sınırı, tıklama işlemi başarılı
      score += 1 #puani 1 arttır.
      score_display.clear() #önceki puanı temizle
      score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal")) #yeni puanı yazdırır.


#ekranda tıklama olayını tanımla
turtle_screen.onscreenclick(tickle)  #tıklama olayını bağlamak

#ilk hareket çağrısı
random_my_turtle()

#ekranı açık tut
turtle.mainloop()




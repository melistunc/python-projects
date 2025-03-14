import turtle
#ekran ile ilgili olan kodlar
drawing_board = turtle.Screen() #bir ekran oluşturuyor.
drawing_board.bgcolor("#800000") #arka plan rengini yeşil yaptı.
drawing_board.title("python turtle") #ekran üstündeki başlık.


#kaplumbağa ile ilgili olan kodlar
#turtle_instance = turtle.Turtle() #bu ok gibi gözüken şeyi oluşturur. şekil çizer.


#square (kare) çizmek
'''for i in range(4):  #0-1-2-3 diye bir liste oluşturur range. Bu liste içinde kodlar 4 defa devam edecek demektir.
    turtle_instance.forward(200)  # kaplumbağa 200 pixel ileri git dedik.
    turtle_instance.left(90) #bu kısım 4 defa çalışır.'''
#bu kısım uzun halidir.
'''turtle_instance.forward(200) #kaplumbağa 200 pixel ileri git dedik.
turtle_instance.left(90)
turtle_instance.forward(200) #önce düz gider sonra sola döner sonra soldan devam eder.
turtle_instance.left(90)
turtle_instance.forward(200) #tekra sola döner ve 200 px ilerler.
turtle_instance.left(90)
turtle_instance.forward(200) #bir daha sola döner ve ilerler böylece kare çizilmiş olur. '''


#star (yıldız) çizimi
'''for i in range(5):  #0-1-2-3-4 diye bir liste oluşturur range. Bu liste içinde kodlar 5 defa devam edecek demektir.
    turtle_instance.left(144)  #bu kısım 4 defa çalışır. 144 derece sola git.
    turtle_instance.forward(180)  # sola gittikten sonra  kaplumbağa 180 pixel ileri git dedik.'''


#polygon çizimi
'''num_sides = 6 #kaç kenarı var onu belirledik.
angle = 360.0 / num_sides #kaç derecede bir değiştireceğiz onu yazdık.
side_len = 100 #ne kadar ileri gitiiğini yazdık.

for i in range(num_sides):  #num_sides diye bir liste oluşturur range. Bu liste içinde kodlar num_sides defa devam edecek demektir.
    turtle_instance.left(angle)  #bu kısım num_sides defa çalışır. angle derece sola git sonra kaplumbağa angle pixel ileri git dedik.
    turtle_instance.forward(side_len)  # sola gittikten sonra  kaplumbağa side_len pixel ileri git dedik.'''

turtle.done() #işimiz bittikten sonra diyoruz. işimiz bitince ekran kapanmıyor.
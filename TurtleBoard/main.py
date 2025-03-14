import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#6B8E23")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()

def turtle_forward(): #onkey için kullanılacak fonksiyon.
    turtle_instance.forward(100) #turtle 100 px gitsin.

def rotate_angle_right():#onkey için sağa harekette kullanılması için.
    turtle_instance.right(10) # 90 derecelik açı ile dön

def rotate_angle_left():#onkey için sola harekette kullanılması için.
    turtle_instance.left(10) # 90 derecelik açı ile dön

def clear_screen(): #ekranda fazlalık olursa bu fazlalığı silmek için kullanılır.
    turtle_instance.clear()

def turtle_return_home(): # okumuz gözden kaybolunca onu tam ortaya geri getirmek için kullanılır.
    turtle_instance.penup() #bunlar home'a gelince etrafı çizmeden otomatik olarak gelmek için kullanılır.
    turtle_instance.home() #home metodu ile kullanılır.
    turtle_instance.pendown() #kalmei kaldır home'a dön kalemi bırak.

def turtle_pen_up(): #okumuzu istediğimiz zaman kaldırıp indirmek için bu alt iki fonksiyonu oluşturduk.
    turtle_instance.penup() #kalmei kaldırmak için kullanılan metot.

def turtle_pen_down():
    turtle_instance.pendown() #kalemi indirmek için kullanılan metot.
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space") #space'e basıldığında bir fonksiyon çalışsın. fun kısmına da yapılacak fonksiyonu koymamız lazım ama çalıştırmaz sadece referans olur. onkey metodu ekran ile etkileşimi sağlar.
#yani burası der ki space'e basınca 100 px ileri gitsin.
drawing_board.onkey(fun=rotate_angle_right,key="Down") #down tuşuna basınca right çalışsın.
drawing_board.onkey(fun=rotate_angle_left,key="Up") #up tuşuna basınca left çalışsın.
drawing_board.onkey(fun=clear_screen, key="c") # c tuşuna basınca ekran temizlensin.
drawing_board.onkey(fun=turtle_return_home,key="v") # v'ye basınca ok ortaya home'a gelsin.
drawing_board.onkey(fun=turtle_pen_up,key="n") # n'ye bastığımızda çizmeyi bırakacak.
drawing_board.onkey(fun=turtle_pen_down,key="m") # m 'ye bastıgımızda ok home'a çizmeden geri gelecek.

turtle.mainloop()
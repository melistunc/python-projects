from sympy import symbols, diff

# x'i sembolik bir değişken olarak tanımlıyoruz
x = symbols('x')

# Fonksiyonu tanımlıyoruz
f = (x+5)**2

# f'nin türevini alıyoruz
f_prime = diff(f, x)

alt_s=0
üst_s=0.01


while True:
    x_value=input("Bir x değerini girin: ")

    if x_value.lower() == 'q':
        print("Çıkış yapıldı.")
        break

    try:
        x_value=float(x_value)
        result = f_prime.subs(x, x_value)
        x1 = x_value - 0.1 * result
        print(f"x = {x_value} için türevdeki değer:", x1)


    except:
        print("Lütfen geçerli bir tam sayı girin veya çıkmak için 'q' yazın.")
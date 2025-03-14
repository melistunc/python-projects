
from rembg import remove

input_path ="image.jpg"
output_path ="output.png" #arkasını sildikten sonra çıkan resim için. ismini biz verdik.

with open(input_path, 'rb') as i: #input_path'i açtık. rb read binary demektir. ismine de i dedik.
    with open(output_path, 'wb') as o: #output_path'i de açtık ve bunu write binary olarak yazdırdık ismine de o dedik. write yazdırmamızın sebebi bunu biz yazıcaz.
        inputFile = i.read() # i'yi oku inputFile içinde.
        outputFile = remove(inputFile) #inputFile'ı remove et diyoruz outputFile içinde. remove fonksiyonunu import etmiştik yukarıda.
        o.write(outputFile) #outputFile'ı yazıp tanımladığımız 'o' nun içine yazıyoruz. Bu sayede outputpath'e kadar ulaşır arkaplanı silinen resmi ekrana yazdırırız.



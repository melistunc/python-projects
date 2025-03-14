from pdf2docx import Converter

pdf_file = "sample.pdf" #girilecek pdf dosyası.
docx_file = "sample2.docx" #alınacak çevrilmiş docx dosyası. Bunu biz write edeceğiz.

cv = Converter(pdf_file) #Converter sınıfından obje oluşturup pdf dosyasını içine koyduk.
cv.convert(docx_file) #oluşturduğumuz objeyi docx_file içine aktardık.
cv.close() #hafızadan bu işlemi manuel olarak silmek için. Sadece kapatmak için kullanılır. Zorunlu değil.



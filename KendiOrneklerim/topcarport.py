sayi1=int(input("Birinci Sayıyı Giriniz : "))
sayi2=int(input("İkinci Sayıyı Giriniz : "))
sayi3=int(input("Üçüncü Sayıyı Giriniz : "))

toplam=sayi1+sayi2+sayi3
carp=sayi1*sayi2*sayi3
ort=(sayi1+sayi2+sayi3) / 3
print("Bu üç sayının toplamı : ", toplam)
print("Bu üç sayının çarpımı : ", carp)
print("Bu üç sayının ortalaması : ", int(ort))

print("Toplam: {}, \nÇarpım: {}, \nOrtalama: {}".format(toplam,carp,ort))
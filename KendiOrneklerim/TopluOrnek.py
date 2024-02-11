"""
sayi = int(input("Kaç defa yazdırayim abe ? "))
isim=input("isim gir : ")
for i in range(sayi):
    print(isim)

"""

"""
for i in range(101):
    print(i)
"""
"""
cift=[]
tek=[]
for sayi in range(100):
    if (sayi %2 == 0):
        cift.append(sayi)
    elif(sayi %2 == 1):
        tek.append(sayi)

print("Tek Sayılar :", tek)
print("Çift sayılar", cift)
"""
"""
baslangic = int(input("Başlangıç sayısı gir : "))
bitis = int(input("Bitiş sayısı gir : "))
j = 0
for i in range(baslangic+1,bitis):
    j +=i


print("Sayıların toplamı : ", j)
"""
"""
urunlistesi = []
while True:
    urun = input("Lütfen ürün ismi giriniz : ")
    urunlistesi.append(urun)
    if(urun == "q"):
        break
print("Programdan çıkıldı")
print("Girdiğiniz ürünler",urunlistesi)
"""
"""
liste = [1,2,3]
adet = len(liste)
toplam = 0
print("Listedeki eleman sayısı : ",adet)
for i in liste: #BURAYA DİKKKAT.. PARANTEZE VEYE KÖŞELİ PARANTEZE GEREK YOK
    toplam += i

sonuc = toplam / adet
print("Ortalama : ", sonuc)
"""


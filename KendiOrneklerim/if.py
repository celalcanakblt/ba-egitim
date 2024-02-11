"""
x = int(input("Lutfen X sayisini giriniz: "))
y = int(input("Lutfen Y sayisini giriniz: "))
if(x == 10 and x == 10):
    print("X sayısı ve Y sayısı 10'a eşittir.")
elif(x==18 and y!=10):
    print("X sayısı 10'a eşittir fakat Y sayisi 10'a eşit değildir.")
elif(x!=10 and y==10):
    print("Y sayisi 10'a eşittir fakat X sayisi 10'a eşit değildir.")
else:
    print("İki sayi da 10'a eşit değildir.")
    """


fiyat=int(input("almak istediğiniz ürünün fiyatını girin : "))
if(fiyat>=50):
    print("Sipariş onayland: toplam ödeyeceğiniz tutar : ", fiyat)
elif(fiyat<50):
    print("Sipariş onaylandı. Ödeyeceğiniz toplam tutar : ", fiyat+7)
else: print("Lütfen geçerli bir tutar giriniz.")
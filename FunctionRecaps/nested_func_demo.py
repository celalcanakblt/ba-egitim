#bir kafe sipariş sistemi oluşturalım. menüde yiecek ve içecek seçenekleri olacak
#yiyecek için ayrı menü, içecek için ayrı bir menü olacak.
#müşteri sipariş verdiğinde fiyat hesaplayacak

#yiyecek menüsü: Burder: 100TL, Pizza: 120TL
#içecek Menü : Kola: 20TL Ayran: 15TL

def siparis_sistemi():
    print("Hosgeldiniz")
    def yiyecek_menu():
        print("Yiyecek Menü:")
        print("Burger: 100TL")
        print("Pizza: 200Tl")
        yiyecek_secim = int(input("Lütfen Seçenek Yapınız"))
        if yiyecek_secim == 1:
            return 100
            print("burger eklendi")
        elif yiyecek_secim == 2:
            return 200
            print("pizza eklendi")
        else:
            print("Geçersiz gridi")
    def icecek_menu():
        print("İçecek Menü:")
        print("Kola: 20TL")
        print("Ayran: 10Tl")
        icecek_secim = int(input("Lütfen Seçenek Yapınız"))
        if icecek_secim == 1:
            return 20
            print("burger eklendi")
        elif icecek_secim == 2:
            return 10
            print("pizza eklendi")
        else:
            print("Geçersiz gridi")
            
    toplam = 0
    while True:
        print("Ana Menü:")
        print("1-Yiyecek Menüsü")
        print("2-İçecek Menüsü")
        print("3-Çıkış")
        ana_secim = int(input("Lütfen alt menü seçiminizi yapınız: "))
        if ana_secim == 1:
            toplam += yiyecek_menu()
        elif ana_secim == 2:
            toplam += icecek_menu()
        elif ana_secim == 3:
            print(f"Toplam ödemeniz gereken tutar: {toplam} TL.")
            print("Bizim Cafe'yi tercih ettiğiniz için teşekkür ederiz.")
            break
        else:
            print("Yanlış bir seçimde bulundunuz.")





siparis_sistemi()
benzin=float(input("Benzinin litre fiyatı kaç tl : "))
kmbasinakaclitre=float(input("Aracınız KM başına kaç litre benzin yakıyor ? : "))
km=float(input("Kaç KM yol gideceksiniz : "))
benzinmiktari=float(input("kaç litre benzininiz var : "))

kalanbenzin= benzinmiktari - kmbasinakaclitre * km

print("kalan benzininiz : ", kalanbenzin)

tutar = (kmbasinakaclitre*km) * benzin

print("toplam tutarınız : ", tutar)
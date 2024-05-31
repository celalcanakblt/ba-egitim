# Alıştırma
# Müşteriler farklı türde ve sayıda ürün satın alabilirler. Her ürünün adı, fiyatı ve miktarı
# olacaktır. Ayrıca, faturaya özel notlar veya kampanya kodları gibi ekstra bilgiler de eklenebilir.

def fatura_olustur(*urunler, **ekstra):
    toplam=0
    for urun in urunler:
        urun_fiyat = urun["miktar"] * urun["fiyat"]
        toplam += urun_fiyat
        print(f"{urun.get('ad', 'Bulunamadı')}\t {urun['miktar']} Adet\t${urun['fiyat']}")
    print(f"Toplam fatura tutarı: ${toplam}")




urun1= {"ad": "Laptop", "fiyat": 1000, "miktar":1}
urun2= {"ad": "Telefon", "fiyat": 500, "miktar":2}
urun3= {"ad": "Klavye", "fiyat": 100, "miktar":3}
urun4= {"ad": "Fare", "fiyat": 50, "miktar":2}










fatura_olustur(urun1, urun2, urun3, Kargo="Express", Kampanya="YAZ2023")
fatura_olustur(urun1, urun2, urun3, Kampanya="YAZ2023", Kargo="Express")

fatura_olustur(urun1, urun2, urun3, Kargo="Express")
fatura_olustur(urun1, urun2, urun3, urun4, Kargo="Express", Kampanya="YAZ2023")
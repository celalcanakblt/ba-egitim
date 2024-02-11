##################### ORTALAMA SICAKLIK ###############################
sehir = input("Lütfen şehir ismi giriniz, ")
enyuksek = float(input("Gün içindeki en yüksek sıcaklığı giriniz : "))
endusuk = float(input("Gün içindeki en düşük sıcaklığı giriniz : "))
ort = (enyuksek + endusuk) / 2
print("{} Şehrinde bugün için ortalama sıcaklık {} derece olarak ölçülmüştür. ".format(sehir,ort))

string1="Merhaba ben celal can akbulut"

uzunluk = len(string1)

print("String uzunluğu = ", uzunluk) #stringin uzunluğunu almak için kullanılır.

print(string1.upper()) #string deperini büyük harflere çevirir

print(string1.lower()) #string deperini küçük harflere çevirir

print(string1.strip()) #bir stringin başındaki ve sonundaki boşlukları kaldırır

print(string1.endswith("t"))

print(string1.endswith("b"))

print("String1 içindeki a harfinin toplam sayısı : ", string1.count("a")) #string değerinin içindeki bir harfin kaç kere geçtiğini yazar.

print("K".join(string1))

print(string1.startswith("M")) #string belirtilen değer ile başlıyorsa true dönder

print(string1.startswith("z")) #string belirtilen değer ile başlıyorsa false dönder

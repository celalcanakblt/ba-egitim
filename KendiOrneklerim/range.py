mylist = range(1,5)
for number in range(len(mylist)):
    print(number)
"""
0
1
2
3
"""

days=["sunday", "monday", "tuesday"]
fruits=["banana", "apple", "watermelon"]
calories=[100,200,300]
zipped_list = list(zip(days,fruits,calories)) #yukarıdaki verileri tek bir yerde ziple. SIRASI ÖNEMLİ ! ! ! ! ! ! !
print(zipped_list)
#ÇIKTI : [('sunday', 'banana', 100), ('monday', 'apple', 200), ('tuesday', 'watermelon', 300)]


isim="celal" #değişken oluşturulduç
new_list=[] #boş liste oluşturuldu
for n in isim:
    new_list.append(n) #isim değişkenindeki her elemanı ayrı ayrı al boş listeye ekle
print(new_list)
#ÇIKTI : ['c', 'e', 'l', 'a', 'l']

yeni = []
yeni = [n for n in isim]
print(yeni)
#ÇIKTI : ['c', 'e', 'l', 'a', 'l']

newnumberlist=[10,20,30,40,50] #yeni liste oluşturuldu
newnumber = [num / 2 for num in newnumberlist] #yeni bir liste daha oluşturuldu. yukarıdaki listenin içindeki elemanları 2ye böl ve bu listeye ekle
print(newnumber)
#ÇIKTI : [5.0, 10.0, 15.0, 20.0, 25.0]
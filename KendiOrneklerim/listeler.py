liste=["celal", "can", 1, 2, 3, 4, 5, "akbulut"]

print(type(liste))

uzunluk=len(liste)

print("liste uzunluğu = ", uzunluk)

liste4=list("celal can akbulut")
print(liste4)

#indeskleme ve parçalama
listem=[1,2,3,4,5,6,7,8,9,10]
print(listem[1]) #birinci elemeanı yaz
print(listem[-1]) #sondan birinci elemanı yaz
print(listem[5:9]) #3. indexten 6. indexe kadar yaz
print(listem[:3]) #3. indexe kadar yaz
print(listem[3:]) #3. indexten sonrasını yaz
print(listem[::3]) #3er 3er atlyarak yaz
print(listem[::-1]) #tersen yaz

#liste methodları ve matematiksel işlemler
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10]
liste3=liste1+liste2 #liste1 ve liste2nin elemanlarını topla aynı listede yaz.
print(liste3)
#listeye dışarıdan elemean eklenebilir.
liste1 += [12]
print(liste1)

#appende methodu verdiğimiz değeri listenin içine atar,
liste1.append(25)
print(liste1)

demet1=(1,2,2,1,12,12,12,312,312,4,13,131,1,1,2,3,1,2,3,2,1,23,4,2,1,2,3)
print(type(demet1))
print(demet1.count(1)) #demet1 listesinin içinde kaç tane 1 değeri var ekrana yaz
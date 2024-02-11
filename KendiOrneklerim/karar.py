print("Karsilaştırma Operatörleri")
#"==" --> sağdaki ve soldaki iki değer birbirine eşit ise True değerini, Değil ise False değerini dönderir.
# "!=" --> sağındaki ve solundaki iki değerin birbirine eşit olmadığı durumda True, esit olduğu durumda ise False değerini dönderir.
# "<" --> soldaki değer sağdaki değerden küçük ise True, büyük ise false değerini dönderir.
# ">" --> soldaki değer sağdaki değerden büyük ise True, küçük ise false değerini dönderir.
# ">" --> soldaki değer sağdaki değerden büyük veya eşit ise True, küçük ise false değerini dönderir.
# "<" --> Soldaki değer sağdaki değerden küçük veya eşit ise True, büyük ise false değerini dönderir.

print("== Operatörü")
print(1 == 1)
print(1 == 2)
print("!= Operatörü")
print(1 != 1)
print(1 != 2)
print("< Operatörü")
print(1 < 1)
print(1 < 2)
print("> Operatörü")
print(1 > 1)
print(1 > 2)
print(2 > 1)
print("> Operatörü")
print(1 >= 1)
print(1 >= 2)
print("<= Operatörü")
print(1 <= 1)
print(1 <= 2)

#and Operatörü --> ve anlamına gelir. soldaki ve sağdaki değerler doğru ise True, Sağda veya Solda herhangi bir değer veya iki değer de yanlış ise False değerini dönderir.
print(1> 0 and 2 > 1)
print("Yusuf" == "Yusuf" and "Yusuf" == "yusuf")
print("yusuf" == "Yusuf" and "Yusuf" == "yusuf")

#or Operatörü --> veya anlamına gelir. Sağdaki veya soldaki değerlerden en az biri doğru ise True, ikisi de yanlış ise False değeri dönderir.
print(1>2 or 1>0)
print(1==5 or 1==6)

#not Operatörü --> yazmış olduğumuz ifade doğru ise False, yanlis ise True değerini dönderir.
print   (not (120))
print(not (120 or 1<0))
print(not (120 and 1<0))
print(not (False and True))
print(not (False))
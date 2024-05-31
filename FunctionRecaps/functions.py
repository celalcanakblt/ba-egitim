# FONKSİYON TANIMLAMA
def name_of_function():
    pass


print(type(name_of_function()))


# Input almayan ve bir şey döndürmeyen fonksiyon
def say_hello():
    """"Bu fonksiyon hello print eder"""
    print("Hello")


# fonksiyonu çağırmak
say_hello()
print(say_hello())


# argüman alan ve bir şey print eden ve bir şey döndürmeyen fonksiyon
def say_hi(name):
    """"Bu fonksiyon 'hi, name' print eder"""
    print("Hi", name)


say_hi("Bob")
say_hi(name="Charlie")
say_hi()  # Boş bıraklamaz çünkü bir argüman bekleniyor


# iki argüman alan ve farklı ifade print eden fonk
def say_mrb(name1: str, name2: str):
    """bu fonksiyon 'Hello, name1' ve 'Goodbye name2' print eder"""
    print("Hello", name1)
    print("Goodbye", name2)


say_mrb("James", "John")
say_mrb(name1="James", name2="Michelle")


# KEYWORD ARGUMENTS
def func2(name1="james", name2="michelle"):
    print("Hello", name1)
    print("Goodbye", name2)


func2(name1="nancy")


def fun3(name1, name2="Michelle", name3="Celal"):
    print("Goodbye", name2)
    print("Hello", name3)
    print("Welcome", name1)


fun3("Halil")


# return keyword: bir fonk çalıştıktan sonra nesne(ler) döndürmesini sağlıyor

def square(x: int):
    """This function gets an int and return sqaure of that int"""
    sqvalue = x * x
    return sqvalue


print(square(9))

x = 10
y = square(x)
print(f"The square of {x} is : {y}")
print(f"The type of {y} is : {type(y)}")


def add_numbers(num1: float, num2: float, num3: float):
    return num1 + num2 + num3


print(add_numbers(10, 15, 16))
print(add_numbers("a", "b", "c"))


# Tek satırda fonksiyon
def multiply_numbers(num1, num2, num3): return num1 * num2 * num3


print(multiply_numbers(3, 3, 3))

# kendi oluşturduğumuz fonksiyonu map() ile kullanma

nmbrs = list(range(0, 20, 3))
print(nmbrs)

print(nmbrs[1] ** 2)


# LİSTENİN İÇİNDEKİ SAYILARIN KARELERİNİ ALAN
def square(num): return num ** 2


print(list(map(square, nmbrs)))


# LİSTEDEKİ SAYILARI 10 İLE ÇARPMAK
def carp(num): return num * 10


print(list(map(carp, nmbrs)))


#Alıştırma: eve_check() isimli bir kullanıcı tanımlı fonksiyon

def even_check(num1):

    if num1 %2 == 0:
        print(f"Bu sayı çift : {num1}")
    else:
        print(f"Bu sayı tek : {num1}")

even_check(5)

mylist = [1,3,5,6,7,8,9,0]
mylist2 = [1,3,5,7,9]
mylist_2 = [1,3,5,7,9]

import time
def even_check_list(num_list):
    for i, num in enumerate(num_list):
        print(f"{i} pozisyonundaki {num} değeri kontrol ediyor")

        if num % 2 == 0:
            print(f"{i} pozisyonundaki {num} değeri çift")

            print("Döngüden çıkılyor")
            return True
        print(f"{i} pozisyonundaki {num} değeri çift değil")

    return False

mybool2 = even_check_list(mylist_2)
print(mybool2)

mybool = even_check_list(mylist)
print(mybool)


#lamba keyword (ananom fonksiyonlar)

squared = lambda x: x**2
type(squared)
print(squared(4))

#map fonksiyonunda anonim lambda fonksiyon kullanmak
nums = list(range(0,20,3))
squared_numbers = list(map(lambda x:x**2, nums))
print(squared_numbers)


evnm = list(filter(lambda x: x%2==0, nums))
print(evnm)
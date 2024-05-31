# Find the Max of three numbers
def max_x_y(x, y):
    if x > y:
        return x
    return y


def max_x_y_z(x, y, z):
    return max_x_y(x, max_x_y(y, z))


print(max_x_y_z(1, 2, 3))


# Find the sum of all the numbers in a list
def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
toplam = sum(liste)
print(toplam)


# Multiply all the numbers in a list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


listem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

carpim = multiply(listem)
print(carpim)


# Python program to reverse a string.
def reverse(mytext):
    print(mytext[::-1])


ters = reverse("1234abcd")
print(ters)


# Calculate the number of upper / lower case letters in a string
def upperlower(mytext):
    numoflower = 0
    numofupper = 0

    for i in mytext:
        if i.islower():
            numoflower += 1
        elif i.isupper():
            numofupper += 1
        else:
            pass
    print(f"Toplam Küçük Harf Sayısı: {numoflower}\n Toplam Büyük Harf Sayısı: {numofupper}")


text = input("Lütfen bir text giriniz")
upperlower(text)


# Unique elements from a list
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 2, 2, 3, 3, 4, 5, 6, 7]))


# Print the even numbers from a given list
def even_numbers(list):
    liste = []
    for x in list:
        if x % 2 == 0:
            liste.append(x)
    return liste


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


#Write a Python function that checks whether a passed string is a palindrome or not.
def palindrom(text):
    if text == text[::-1]:
        print("This is a palindrom")
    else:
        print("This is not a palindrom")

palindrom("adaa")

import string
import sys

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)

    str_set = set(str1.lower())
    return alphaset <= str_set

print(ispangram('The quick brown fox jumps over the lazy dog'))
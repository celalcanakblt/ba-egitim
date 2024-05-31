def topla(*args):
    print(f"*args'ın tipi : {type(args)}. Çıktısı : {args}")
    print(f"args tuple'nın ilk elemanı: {args[0]}")
topla(1,2,3,4,5,6,7,8,9)


def print_info(**kwargs):
    return kwargs



def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"Anahatar: {key}, Değer: {value}")

print_info(name="Ailce", age="20", city="Ankara", country="Turkey", hobbies=["footbal","python"])


def mixed_func(*a, **k):
    print(f"positional arguments: {a}")
    print(f"keywrod arguments: {k}")


#anahtar kelime ile kullanıldığında kwargs,
#positional args, kwargs'dan sonra gelmez
mixed_func(1,2,4)

mixed_func(1,2,4, name="ali", age=20, city="ankara")


# a ve b positional arguments
# c=5 keyword arguments
# *args arbitrary arguments
# **kwargs arbitrary keyword arguments
def mixed_funcc(a,b, c=5, *args, **kwargs):
    print(f"{a}, {b}")
    print({c})
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_funcc(7,8)
mixed_funcc(7,8,6)
mixed_funcc(7,8,6, 2, 3)
mixed_funcc(7,8,6, 2, 3, name="ali", city="ankara", age=20)



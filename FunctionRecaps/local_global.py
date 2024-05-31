def example():
    a = 10
    print(f"Fonksiyon içi değişken a=", a)

b=5

def example_global():
    global b
    b *= 2
    
    print(f"Fonksiyon içi değişken b=", b)

example_global()

print(b)
#################### PALINDROM KONTROL ####################
example = input("Lütfen bir kelime veya cümle giriniz : ")
cleared = ""
for x in example:
    if x.isalnum() or x == "":
        cleared += x
print(cleared)
if cleared == (cleared[::-1]):
    print("Evet girdiğiniz kelime / cümle bir palindromdur : ", cleared.lower())
else:
    print("Girdiğiniz kelime / cümle bir palindrom değildir : ", cleared.lower())
######################################################################################################
#################### BANKA BİLGİ SİLME GÜNCELLEME ####################
customer = {'name': 'Ahmet', 'surname': 'Çelik', 'age': 25, 'account_balance': 1200.0}
def update():
    x = input("Hangi veriyi güncellemek istiyorsunuz : ")
    if x in customer:
        new_value = input("Lütfen yeni veriyi giriniz :")
        customer[x] = new_value
        print(customer)

def delete():
    y = input("Hangi veriyi silmek istiyorsunuz : ")
    if y in customer:
        customer.pop(y)
        print(customer)

update()
delete()
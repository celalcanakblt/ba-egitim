#Recursive Functions# Çalışan-ast ilişkisini tanımlayan sözlük
import time    # time Python Standard Library

calisan_hiyerarsi1 = {
    'CEO': ['CTO', 'CFO', 'CMO'],
    'CTO': ['Dev1', 'Dev2'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

calisan_hiyerarsi2 = {
    'CEO': ['CTO', 'CFO'],
    'CTO': ['Dev1', 'Dev2', 'Dev3'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4'],
    'Dev2': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

def toplam_ast(hiyerarsi: dict, calisan: str):
    #toplam ast sayısını bulmak için bir değişken tanımlayalım
    toplam = 0
    #Girilen "çalışan", stringi "hiyerarşi" sözlüğünün anahtarlar arasında yer almıyorsa
    #ast'ı yoktur. dolayısıyla 0 döndürür
    if calisan not in hiyerarsi:
        return 0


    astlar = hiyerarsi[calisan]


toplam_ast(calisan_hiyerarsi1, calisan="CTO")
toplam_ast(calisan_hiyerarsi2, calisan="CEO")

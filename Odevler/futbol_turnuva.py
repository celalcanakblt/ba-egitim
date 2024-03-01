######################## 3. ALIŞTIRMA UZUN YOL ########################
matches = {
 'barca_rma': (3, 2),
 'rma_manu': (1, 1),
 'manu_barca': (2, 2)
}
team_points = {
 'barcapoint': 0,
 'rmapoint': 0,
 'manupoint': 0
}

if matches['barcavsrma'][0] > matches['barcavsrma'][1]:
    team_points['barcapoint'] += 3
elif matches['barcavsrma'][0] == matches['barcavsrma'][1]:
    team_points['barcapoint'] += 1
    team_points['rmapoint'] += 1
else:
    team_points['rmapoint'] += 3
if matches['rmavsmanu'][0] > matches['rmavsmanu'][1]:
    team_points['rmapoint'] += 3
elif matches['rmavsmanu'][0] == matches['rmavsmanu'][1]:
    team_points['rmapoint'] += 1
    team_points['manupoint'] += 1
else:
    team_points['manupoint'] += 3
if matches['manuvsbarca'][0] > matches['manuvsbarca'][1]:
    team_points['manupoint'] += 3
elif matches['manuvsbarca'][0] == matches['manuvsbarca'][1]:
    team_points['manupoint'] += 1
    team_points['barcapoint'] += 1
else:
    team_points['barcapoint'] += 3

print(team_points)

######################## 3. ALIŞTIRMA KISA YOL ########################

matches = { #matches adında bir sözlük oluşturuluyor. Bu sözlük, maçların isimlerini anahtar olarak ve her maçın skorlarını değer olarak içeriyor.
 'barca_rma': (1, 1), #team_points adında bir sözlük oluşturuluyor. Bu sözlük, her takımın puanını saklamak için kullanılacak. Başlangıçta her takımın puanı sıfır olarak ayarlanıyor.
 'rma_manu': (1, 1),
 'manu_barca': (2, 2)
}
team_points = {
 'barca': 0,
 'rma': 0,
 'manu': 0
}

for match, (skor1, skor2) in matches.items(): # maçların ismi 'match' isimli değişkende tutuluyor. maçın skorları skor1 ve skor2 adlı değişkenlere atanıyor.
    team1,team2 = match.split('_') # bu satırın anlamı _ işaretinin sol tarafı TAKIM 1  sağ tarafı ise TAKIM 2 ismini tutuyor.
    if skor1 > skor2:
        team_points[team1] += 3 # team_points[team1]: team_points sözlüğündeki team1 anahtarına karşılık gelen değeri temsil eder. team1 değişkeni, maç isminin ilk takımını temsil eder.
    elif skor1 < skor2:
        team_points[team2] += 3
    else:
        team_points[team1] += 1
        team_points[team2] += 1
print(team_points)
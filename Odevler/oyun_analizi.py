#################### OYUN ANALİZİ ####################
user_data = {
    'John': {'Minecraft': 120, 'Among Us': 45, 'Valorant': 90},
    'Emily': {'Minecraft': 55, 'Tetris': 90, 'Call of Duty': 80},
    'Peter': {'Tetris': 100, 'Among Us': 30, 'FIFA': 75},
    'Sophie': {'Among Us': 50, 'Minecraft': 70, 'FIFA': 60},
    'Mike': {'Tetris': 110, 'Minecraft': 30, 'Call of Duty': 70},
    'Sara': {'FIFA': 45, 'Minecraft': 40, 'Among Us': 35},
    'Alex': {'Call of Duty': 100, 'Valorant': 70, 'FIFA': 80},
    'Natalie': {'Tetris': 45, 'FIFA': 50, 'Minecraft': 30},
    'Chris': {'Call of Duty': 60, 'Valorant': 75, 'Among Us': 50},
    'Isabella': {'Tetris': 35, 'Minecraft': 60, 'FIFA': 45}
}
#################### HER OYUNU KAÇ FARKLI KULLANICI OYNADI ####################
# Her oyunun kaç farklı kullanıcı tarafından oynandığını tutacak bir sözlük oluştur
games_counter = {}
for user_games in user_data.values(): #oyun tercihlerini tek tek incele
    for game in user_games: #her bir kullanıcının oyun tercihlerini tek tek al ve game olarak dolaş
        if game in games_counter: #eğer game olarak dolarşırken
            games_counter[game] += 1 #games_counter sözlüğü içerisinde varsa ilgili oyunun sayacını 1 arttır.
        else:
            games_counter[game]=1 #eğer oyun games_counter içerisinde yoksa sayacı başlat ve 1e eşitle
for game, count in games_counter.items():
    print(f"{game} oyunu {count} farklı kişi tarafından oynanmıstır")

#################### HANGİ OYUN KAÇ DAKİKA OYNANDI ####################
total_playtime = {}

for x in user_data.values():
    for oyun,sure in x.items():
        if oyun not in total_playtime:
            total_playtime[oyun] = 0
        total_playtime[oyun] += sure

for oyun,totaltime in total_playtime.items():
    print(f"{oyun} oyunu toplam {totaltime} dakika oynanmıstır")

#################### EN ÇOK OYNANAN OYUN VE DAKİKASI ####################
most_played_game = max(total_playtime, key=total_playtime.get)
total_time_most_played_game = total_playtime[most_played_game]
print(f"En çok oynanan oyun: {most_played_game}, Toplam süre: {total_time_most_played_game} dakika")
#################### EN AZ OYNANAN OYUN VE DAKİKASI ####################
min_played_game = min(total_playtime, key=total_playtime.get)
min_time_most_played_game = total_playtime[min_played_game]
print(f"En az oynanan oyun: {min_played_game}, Toplam süre: {min_time_most_played_game} dakika")
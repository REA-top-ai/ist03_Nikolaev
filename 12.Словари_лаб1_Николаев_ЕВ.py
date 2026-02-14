# 1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22
print(sensors)

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(num_cameras)

print()

# 2
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)

print()

# 3
animals_in_zoo = {}
animals_in_zoo["зебры"] = 8
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавров"] = 0
print(animals_in_zoo)

print()

# 4
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

print()

# 5
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

print()

# 6
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drink: mg for drink, mg in zipped_drinks}
print(drinks_to_caffeine)

print()

# 7
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: count for song, count in zip(songs, playcounts)}
print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = plays["Respect"] + 5

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)

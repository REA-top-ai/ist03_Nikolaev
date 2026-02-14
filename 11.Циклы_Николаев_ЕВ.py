# 1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

# 2
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

# 3
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

# 4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
    print(breed)
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break

# 5
sales_data = [[12,17,22],[2,10,3],[5,12,13]]
scoops_sold = 0

for place in sales_data:
    for value in place:
        scoops_sold += value

print(scoops_sold)

# 6
single_digits = list(range(10))

squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit * digit)

print(squares)

cubes = [digit**3 for digit in single_digits]
print(cubes)

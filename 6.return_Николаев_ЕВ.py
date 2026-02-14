# 1
def calc_age(current_year, birth_year):
    age = current_year - birth_year
    return age

# 2
my_age = calc_age(2049, 1993)

# 3
dads_age = calc_age(2049, 1953)

print("Мне", my_age, "лет, а моему отцу", dads_age, "лет")

print()

# 4
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

# 5
low_limit, high_limit = get_boundaries(100, 20)

# 6
print("Нижний предел:", low_limit, ", верхний предел:", high_limit)

print()

# 7
def repeat_stuff(stuff, num_repeats):
    print()

# 8
repeat_stuff("Row", 3)

# 9 + 10
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

# 11
lyrics = repeat_stuff("Row", 3) + "Your Boat."

# 12
song = repeat_stuff("Row")

# 13
print(lyrics)
print(song)

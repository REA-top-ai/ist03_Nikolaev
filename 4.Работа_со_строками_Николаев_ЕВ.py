# 1
favour_word = "сила"
print(favour_word)

print()

# 2
first_name = "Виталий"
last_name = "Красилов"

new_account = last_name[:5]
temp_password = last_name[2:6]

print(first_name)
print(last_name)
print(new_account)
print(temp_password)

print()

# 3
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)
print(new_account)

print()

# 4
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password)

print()

# 5
company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

print(second_to_last)
print(final_word)

print()

# 6
first_name_typo = "роб"
fixed_first_name = "Р" + first_name_typo[1:]

print(first_name_typo)
print(fixed_first_name)

print()

# 7
password = "theycallme\"crazy\"91"
print(password)

print()

# 8
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)
print(poem_author)

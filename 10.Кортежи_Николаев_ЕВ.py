# 1

correct_answers = (
1,2,3,2,1,2,1,3,1,2,
1,2,3,3,2,1,2,1,2,1
)

user_answers = [
1,2,3,2,1,2,1,3,1,2,
1,2,3,3,2,1,2,1,2,1
]

if tuple(user_answers) == correct_answers:
    print("Экзамен сдан")
else:
    print("Экзамен провален")

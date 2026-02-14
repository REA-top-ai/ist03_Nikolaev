# 1
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# 2
zodiac_elements["energy"] = "Not a Zodiac element"

# 3
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30

try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

# 4
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

print(tc_id)
print(stack_id)

# 5
users = user_ids.keys()

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
classes = num_exercises.keys()

print(users)
print(classes)

# 6
total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print(total_exercises)

# 7
tarot = {1:"The Magician",2:"The High Priestess",3:"The Empress",4:"The Emperor",5:"The Hierophant",6:"The Lovers",7:"The Chariot",8:"Strength",9:"The Hermit",10:"Wheel of Fortune",11:"Justice",12:"The Hanged Man",13:"Death",14:"Temperance",15:"The Devil",16:"The Tower",17:"The Star",18:"The Moon",19:"The Sun",20:"Judgement",21:"The World",22:"The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

print(spread)

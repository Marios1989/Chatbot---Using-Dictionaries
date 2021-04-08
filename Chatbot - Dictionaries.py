# Introduction to Dictionaries
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry":22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

# Make a Dictionary
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Invalid Keys
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

# Empty Dictionaries
my_empty_dictionary = {}

# Add a Key
animals_in_zoo = {"zebras": 8, "monkeys": 12, "dinosaurs": 0}
print(animals_in_zoo)

# Add Multiple Keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238, "theLooper": 138475, "stringQueen": 85739}
print(user_ids)

# Overwrite Values
oscar_winners = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia", "Supporting Actress": "Viola Davis"}

# List Comprehensions to Dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

# Review
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations", "Purple Haze", "Respect"]
playcounts = [78, 29, 44, 21, 89, 5, 1, 94]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)


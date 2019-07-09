# print("Hello! Please complete this survey for me.")
# print("What is your name?")


# new_dict = {"name": "trang", 13: "tiger", "may":5}

# print(new_dict["name"])

# for each in new_dict:
#     print(new_dict[each])

# dict = {"name": 23}


import time
import json

ls = []

print("Hello please complete this survey.")
dict = {}

def questions(dict):
    answer = input("what's your name?")
    dict["name"] = answer
    time.sleep(0.5)
    answer = input("when is your birthday? (MM/DD/YYYY)")
    dict["bday"] = answer
    time.sleep(0.5)
    answer = input("what is your favorite boba place?")
    dict["boba"] = answer
    time.sleep(0.5)
    answer = input("Who is your celebrity crush?")
    dict["celeb crush"] = answer
    time.sleep(0.5)
    answer = input("What is your biggest fear?")
    dict["fear"] = answer
    time.sleep(0.5)

for i in range(2):
    dict = {}
    questions(dict)
    ls.append(dict)
tojson = json.dumps(ls)


print(tojson)
print(ls)

with open('dictionary.json', 'w') as outfile:
        json.dump(ls, outfile)

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

responses = {}


def ask_question(prompt, key):
    answer = raw_input(prompt + " (y/n) >")
    if answer in ['y', 'Y', 'yes', 'Yes']:
        responses[key] = True
    else:
        responses[key] = False

    print responses


def ask_questions(questions):
    for key, question in questions.items():
        ask_question(question, key)

def make_drink(ingredients, preferences):
    drink = []

    for key, value in preferences.items():
        print key, value
        if value == True:
            choice = random.choice(ingredients[key])
            drink.append(choice)
    return drink

def main():
    ask_questions(questions)
    drink = make_drink(ingredients, responses)

    print "Bartender makes you a drink with: %r" % drink


main()
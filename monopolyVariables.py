import random
from main import *

def roll_die():
    die = random.randint(1,6)
    return die


# These dictionaries keep track of how many each time each die hits a specific number
die_one_rolled_amount = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
die_two_rolled_amount = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
# We begin by creating a dictionary of each property
# The name will be the key, and the value will be set to 0

properties_dictionary = {
    "Go": 0,
    "Mediterranean Avenue": 0,
    "Community Chest 1": 0,
    "Baltic Avenue": 0,
    "Income Tax": 0,
    "Reading Railroad": 0,
    "Oriental Avenue": 0,
    "Chance 1": 0,
    "Vermont Avenue": 0,
    "Connecticut Avenue": 0,
    "In Jail/Just Visiting": 0,
    "St. Charles Place": 0,
    "Electric Company": 0,
    "States Avenue": 0,
    "Virginia Avenue": 0,
    "Pennsylvania Railroad": 0,
    "St. James Place": 0,
    "Community Chest 2": 0,
    "Tennessee Avenue": 0,
    "New York Avenue": 0,
    "Free Parking": 0,
    "Kentucky Avenue": 0,
    "Chance 2": 0,
    "Indiana Avenue": 0,
    "Illinois Avenue": 0,
    "B & O Railroad": 0,
    "Atlantic Avenue": 0,
    "Ventnor Avenue": 0,
    "Water Works": 0,
    "Marvin Gardens": 0,
    "Go To Jail": 0,
    "Pacific Avenue": 0,
    "North Carolina Avenue": 0,
    "Community Chest 3": 0,
    "Pennsylvania Avenue": 0,
    "Short Line": 0,
    "Chance 3": 0,
    "Park Place": 0,
    "Luxury tax": 0,
    "Boardwalk": 0,
}
properties_color = {
    "Go": "None",
    "Mediterranean Avenue": "Brown",
    "Community Chest 1": "None",
    "Baltic Avenue": "Brown",
    "Income Tax": "None",
    "Reading Railroad": "None",
    "Oriental Avenue": "Light Blue",
    "Chance 1": "None",
    "Vermont Avenue": "Light Blue",
    "Connecticut Avenue": "Light Blue",
    "In Jail/Just Visiting": "None",
    "St. Charles Place": "Pink",
    "Electric Company": "None",
    "States Avenue": "Pink",
    "Virginia Avenue": "Pink",
    "Pennsylvania Railroad": "None",
    "St. James Place": "Orange",
    "Community Chest 2": "None",
    "Tennessee Avenue": "Orange",
    "New York Avenue": "Orange",
    "Free Parking": "None",
    "Kentucky Avenue": "Red",
    "Chance 2": "None",
    "Indiana Avenue": "Red",
    "Illinois Avenue": "Red",
    "B & O Railroad": "None",
    "Atlantic Avenue": "Yellow",
    "Ventnor Avenue": "Yellow",
    "Water Works": "None",
    "Marvin Gardens": "Yellow",
    "Go To Jail": "None",
    "Pacific Avenue": "Green",
    "North Carolina Avenue": "Green",
    "Community Chest 3": "None",
    "Pennsylvania Avenue": "Green",
    "Short Line": "None",
    "Chance 3": "None",
    "Park Place": "Dark Blue",
    "Luxury tax": "None",
    "Boardwalk": "Dark Blue",
}

# We also need a list of each property in the correct order
properties_list = [
    "Go",
    "Mediterranean Avenue",
    "Community Chest 1",
    "Baltic Avenue",
    "Income Tax",
    "Reading Railroad",
    "Oriental Avenue",
    "Chance 1",
    "Vermont Avenue",
    "Connecticut Avenue",
    "In Jail/Just Visiting",
    "St. Charles Place",
    "Electric Company",
    "States Avenue",
    "Virginia Avenue",
    "Pennsylvania Railroad",
    "St. James Place",
    "Community Chest 2",
    "Tennessee Avenue",
    "New York Avenue",
    "Free Parking",
    "Kentucky Avenue",
    "Chance 2",
    "Indiana Avenue",
    "Illinois Avenue",
    "B & O Railroad",
    "Atlantic Avenue",
    "Ventnor Avenue",
    "Water Works",
    "Marvin Gardens",
    "Go To Jail",
    "Pacific Avenue",
    "North Carolina Avenue",
    "Community Chest 3",
    "Pennsylvania Avenue",
    "Short Line",
    "Chance 3",
    "Park Place",
    "Luxury tax",
    "Boardwalk",
    ]
def create_community_list():
    community_chest_list = [
        "Advance to Go",
        "Bank Error",
        "Doctors fee",
        "Sale Stock",
        "Get out of Jail",
        "Go to Jail",
        "Holiday Fund",
        "Income Tax Refund",
        "Birthday",
        "Life Insurance",
        "Hospital Fees",
        "School Fees",
        "Receive Money",
        "Street Repairs",
        "Beauty Contest",
        "Inherit Money"
    ]
    random.shuffle(community_chest_list)
    return community_chest_list


def create_chance_list():
    my_list = [
        "Advance to Boardwalk",
        "Advance to Go",
        "Advance to Illinois Avenue",
        "Advance to St. Charles Place",
        "Advance to the nearest Railroad",
        "Advance to the nearest Railroad",
        "Advance to the nearest Utility",
        "Bank Pays",
        "Get out of Jail Free",
        "Go Back 3 spaces",
        "Go to Jail",
        "General Repairs",
        "Speeding Fine",
        "Advance to Reading Railroad",
        "Elected Chairman",
        "Loan matures"
    ]
    random.shuffle(my_list)
    return my_list


def draw_card(card_deck):
    return card_deck.pop()


def card_movement(card, card_position):
    if card == "Advance to Boardwalk":
        # print("Advance to Boardwalk")
        return 39
    elif card == "Advance to Go":
        # print("Advance to Go")
        return 0
    elif card == "Advance to Illinois Avenue":
        # print("Advance to Illinois Avenue")
        return 24
    elif card == "Advance to St. Charles Place":
        # print("Advance to St. Charles Place")
        return 11
    elif card == "Advance to the nearest Railroad":
        # print("Advance to the nearest Railroad")
        value_1 = 5 - card_position
        value_2 = 15 - card_position
        value_3 = 25 - card_position
        value_4 = 35 - card_position
        nearest_railroad = []
        if value_1 >= 0:
            nearest_railroad.append(value_1)
        if value_2 >= 0:
            nearest_railroad.append(value_2)
        if value_3 >= 0:
            nearest_railroad.append(value_3)
        if value_4 >= 0:
            nearest_railroad.append(value_4)
        if len(nearest_railroad) == 0:
            nearest_railroad.append(5)

        smallest_number = min(nearest_railroad)
        if smallest_number == value_1:
            return 5
        elif smallest_number == value_2:
            return 15
        elif smallest_number == value_3:
            return 25
        elif smallest_number == value_4:
            return 35
        else:
            return 5
    elif card == "Advance to the nearest Utility":
        # print("Advance to the nearest Utility")
        value_1 = 12 - card_position
        value_2 = 28 - card_position

        if value_1 >= 0:
            return 12
        elif value_2 >= 0:
            return 28
        else:
            return 12
    elif card == "Advance to Reading Railroad":
        # print("Advance to Reading Railroad")
        return 5
    elif card == "Go to Jail":
        # print("Go to Jail")
        return 10
    elif card == "Go Back 3 spaces":
        # print("Go Back 3 spaces")
        return card_position - 3


my_deck = create_chance_list()

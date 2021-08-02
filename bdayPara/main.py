"""
Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation
"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Return a list of random date objects for birthdays"""
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays):
    """Returns the date objects of a birthday that occurs more than onces in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None

    # compare birthays to the others
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1]):
            if birthdayA == birthdayB:
                return birthdayA


# Display the intro:
print(
    """Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
 47. 
"""
)

# Tuples of the months:
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)


while True:
    print("How many people do you want to simulate?(Max 100)")
    response = input(">")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break

print()

print("Here are", numBdays, "birthdays:")
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print("", end="")
print()
print()

# Determine two birthdays
match = getMatch(birthdays)

# Display the results
print("In this simulation", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    datetext = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()

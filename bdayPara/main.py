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

    for _ in range(numberOfBirthdays):
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
    dateText = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations:
print('Generating', numBdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print('100,000 simulations run.')
# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
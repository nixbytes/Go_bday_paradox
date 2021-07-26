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



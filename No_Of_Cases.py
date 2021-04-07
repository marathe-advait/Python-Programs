import random

def no_of_cases():
    no_of_cases = random.randint(1, 1800)
    no_of_deaths = random.randint(0, int(0.025*no_of_cases))
    return no_of_cases, no_of_deaths

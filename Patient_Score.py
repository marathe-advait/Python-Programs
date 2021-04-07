def patient_score (dist, cases):
    active_cases = cases[0]
    no_of_deaths = cases[1]
    score = int(20 + 4.24264 * (3.53553 - dist) + 0.01667 * active_cases + 0.99887 * no_of_deaths)
    return score
    

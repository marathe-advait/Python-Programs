from Rand_Coor import rand_coor
from Cal_Distance import cal_distance
from No_Of_Cases import no_of_cases
from Patient_Score import patient_score

coor = rand_coor()
print("The location is - {}".format(coor[0]))
print("The patient location is - {}".format(coor[1]))
dist = cal_distance(coor)
print("The distance is - {}".format(dist))
cases = no_of_cases()
print("The number of total cases are - {}".format(cases[0]))
print("The number of deaths are - {}".format(cases[1]))
score = patient_score(dist, cases)
print("The patient is at {}% risk".format(score))

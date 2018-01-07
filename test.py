import random

print("Combien de verbes?")
N = int(input())

temps =  ["Base verbale", "Prétérit", "Participe passé", "Traduction"]

with open("vbs.txt", encoding="utf-8") as text:
    lines = text.readlines()
    verbes = [line[:-1].split("-") for line in lines]

points = 0

for i in range(N):
    vb_index = random.randint(0, len(verbes) - 1)
    tps_index = random.randint(0, 3)
    print(temps[tps_index] + ": " + verbes[vb_index][tps_index])
    nb_good_answers = 0
    for tp in temps:
        if tp != temps[tps_index]:
            answer = input(tp + ": ")
            possible_answers = verbes[vb_index][temps.index(tp)].split("/")
            if answer in possible_answers or answer == verbes[vb_index][temps.index(tp)]:
                nb_good_answers += 1
    if nb_good_answers == 3:
        points += 3
        print("+3 pts!")
    else:
        plus_pts = nb_good_answers * 0.5
        points += plus_pts
        print("+" + str(plus_pts) + " pts...")
    print("Correction: " + str(" -- ".join(verbes[vb_index])))

    print(str(nb_good_answers) + " good answer(s)\n")
        
    print("Total: " + str(points) + "\n")

print("Score: " + str(round(((points / (N * 3)) * 100), 2)) + " %")
print("Mark: " + str(round((points / (N * 3) * 20), 1)) + "/20")
input("Appuyez sur une toucher pour fermer...")
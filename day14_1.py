recipes = [3,7]
Elves_1 = 0
Elves_2 = 1

while True:
    if recipes[Elves_1] + recipes[Elves_2] >= 10:
        recipes.append(int((recipes[Elves_1] + recipes[Elves_2]) / 10))
        recipes.append((recipes[Elves_1] + recipes[Elves_2]) % 10)
    else:
        recipes.append(recipes[Elves_1] + recipes[Elves_2])

    if (recipes[Elves_1] + 1) < (len(recipes) - Elves_1):
        Elves_1 = Elves_1 + recipes[Elves_1] + 1
    elif (recipes[Elves_1] + 2 - (len(recipes) - Elves_1))%len(recipes) == 0:
        Elves_1 = len(recipes) - 1
    else:
        Elves_1 = (recipes[Elves_1] + 2 - (len(recipes) - Elves_1))%len(recipes) - 1

    if (recipes[Elves_2] + 1) < (len(recipes) - Elves_2):
        Elves_2 = Elves_2 + recipes[Elves_2] + 1
    elif (recipes[Elves_2] + 2 - (len(recipes) - Elves_2))%len(recipes) == 0:
        Elves_2 = len(recipes) - 1
    else:
        Elves_2 = (recipes[Elves_2] + 2 - (len(recipes) - Elves_2))%len(recipes) - 1

    if len(recipes) > (209231+10):
        print(recipes[209231:209241])
        break
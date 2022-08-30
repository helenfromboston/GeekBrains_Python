# Задача 3. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?

budget = 1000
costBull = 100
costCow = 50
costLittleCow = 5
focus = 100
sum = 0
for b in range(0, budget // costBull):
    for c in range(0, budget // costCow):
        for l in range(0, budget // costLittleCow):
            sum = b * costBull + c * costCow + l * costLittleCow
            if b * costBull + c * costCow + l * costLittleCow == budget and b + c + l == focus:
                print(f" Bull = {b}, Cow = {c}, LittleCow = {l}, Budget = {sum}")
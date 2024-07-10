exp = [2200, 2350, 2600, 2130, 2190]

print(f"Dollars spent extra in Feb compared to Jan: {exp[1] - exp[0]}")
print(f"First quarter expense: {sum(exp[0:3])}")
print("Did I spend 2000 exactly?", 2000 in exp)
exp.append(1980)
exp[4] = exp[4] - 200
print(exp)


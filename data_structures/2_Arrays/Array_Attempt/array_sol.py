exp = [2200, 2350, 2600, 2130, 2190]

print(f"Dollars spent extra in Feb compared to Jan: {exp[1] - exp[0]}")
print(f"First quarter expense: {sum([exp in exp[0:2]])}")

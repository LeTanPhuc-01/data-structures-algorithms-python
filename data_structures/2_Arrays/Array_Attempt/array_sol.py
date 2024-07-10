exp = [2200, 2350, 2600, 2130, 2190]
#1 In Feb, how many dollars you spent extra compare to January?
print(f"Dollars spent extra in Feb compared to Jan: {exp[1] - exp[0]}")
# 2. Find out your total expense in first quarter (first three months) of the year.
print(f"First quarter expense: {sum(exp[0:3])}")
# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spend 2000 exactly?", 2000 in exp)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
exp[3] = exp[3] - 200

print(exp)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append("black panther")
print(heros)

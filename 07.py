import random
from tabulate import tabulate

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

N = 1000
sums_count = {}

for _ in range(N):
    result = roll_dice()
    if result in sums_count:
        sums_count[result] += 1
    else:
        sums_count[result] = 1

probabilities = {}

for sum_value, count in sums_count.items():
    probabilities[sum_value] = count / N

data  = []
for sum_value in sorted(probabilities.keys()):
    probability_percent = round(probabilities[sum_value] * 100, 2)
    count_info = f"{sums_count[sum_value]}/{N}"
    data.append([sum_value, probability_percent, count_info])

headers = ["Sum", "Probability (%)", "Occurrences"]

print(tabulate(data, headers=headers, tablefmt="grid"))
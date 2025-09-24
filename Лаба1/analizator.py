import csv
import statistics
import os
from concurrent.futures import ProcessPoolExecutor

def analyze(name: str):
    letter_vals = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

    with open(name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            letter = row[0].strip()
            val = float(row[1].strip())
            letter_vals[letter].append(val)

    file_res = {}
    for letter, vals in letter_vals.items():
        if len(vals) >= 2:
            median = statistics.median(vals)
            stdev = statistics.stdev(vals)
            file_res[letter] = {'median': median, 'stdev': stdev}
        elif len(vals) == 1:
            file_res[letter] = {'median': vals[0], 'stdev': 0.0}

    letter_medians = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    print(name)
    print("-" * 15)
    for letter, info in file_res.items():
        if info['median']:
            print(f"{letter}: median: {info['median']} +- {info['stdev']}")
            letter_medians[letter].append(info['median'])
        else:
            print(f"{letter}: -")
    print()

    return letter_medians



names = []
for i in range(5):
    name = f"data_{i}.csv"
    names.append(name)

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results  = list(executor.map(analyze, names))

    letter_medians = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

    for result in results:
        for letter, median in result.items():
            letter_medians[letter].append(median[0])

    final_medians = {}
    for letter,medians in letter_medians.items():
        if medians:
            med = statistics.median(medians)
            if len(medians) >= 2:
                std = statistics.stdev(medians)
            else:
                std = 0.0
            final_medians[letter] = {'median': med, 'stdev': std}

    print("result")
    print("-" * 15)
    for letter, info in final_medians.items():
        if info['median']:
            print(f"{letter}: median: {info['median']} +- {info['stdev']}")
            letter_medians[letter].append(info['median'])
        else:
            print(f"{letter}: -")


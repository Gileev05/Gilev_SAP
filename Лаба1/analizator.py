import csv
import statistics
import os

results = {}

for i in range(5):
    name = f"data_{i}.csv"

    letter_vals = {'A':[], 'B': [], 'C':[], 'D':[], 'E':[]}

    with open(name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            letter = row[0].strip()
            val = float(row[1].strip())
            letter_vals[letter].append(val)

    file_res = {}
    for letter,vals in letter_vals.items():
        if len(vals) >= 2:
            median = statistics.median(vals)
            stdev = statistics.stdev(vals)
            file_res[letter] = {'median': median, 'stdev': stdev}
        elif len(vals) == 1:
            file_res[letter] = {'median': vals[0], 'stdev': 0.0}
    results[name] = file_res

letter_medians = {'A':[], 'B': [], 'C':[], 'D':[], 'E':[]}
for name, res in results.items():
    print(name)
    print("-" * 15)
    for letter,info in res.items():
        if info['median']:
            print(f"{letter}: median: {info['median']} +- {info['stdev']}")
            letter_medians[letter].append(info['median'])
        else:
            print(f"{letter}: -")
    print()



final_file_res = {}
for letter,vals in letter_medians.items():
    if len(vals) >= 2:
        median = statistics.median(vals)
        stdev = statistics.stdev(vals)
        final_file_res[letter] = {'median': median, 'stdev': stdev}
    elif len(vals) == 1:
        final_file_res[letter] = {'median': vals[0], 'stdev': 0.0}

print('result')
print("-" * 15)
for letter,info in final_file_res.items():
    if info['median']:
        print(f"{letter}: median: {info['median']} +- {info['stdev']}")
        letter_medians[letter].append(info['median'])
    else:
        print(f"{letter}: -")
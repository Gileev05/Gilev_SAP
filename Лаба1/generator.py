import csv
import random
import string

for i in range(5):
    name = f"data_{i}.csv"
    data = []
    for j in range(30):
        ran_let = random.choice(['A','B','C','D','E'])
        ran_val = random.uniform(1.0,10.0)
        data.append([ran_let, ran_val])

    with open (name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)





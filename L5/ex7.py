#7
import json


with open('companies.txt', 'r', encoding='utf-8') as f_input:
    d_1 = {}
    summary = 0
    count = 0
    for row in f_input.readlines():
        profit = int(row.split()[2]) - int(row.split()[3])
        d_1[row.split()[0]] = profit
        if profit > 0:
            summary += profit
            count += 1
    lst = [d_1, {'average_profit': int(summary/count)}]

with open('J_out.json', 'w') as f_output:
    json.dump(lst, f_output)
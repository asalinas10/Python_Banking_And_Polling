# import modules

import os
import csv

# set csv file to variable

pybankcsv = os.path.join("Resources", "budget_data.csv")

# 

total_profits = 0

Months = []

total_pl = []

with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    

    gross_pl = 0

    for row in csvreader:
        Months.append(row[0])

        total_pl.append(int(row[1]))

        prof_loss = int(row[1])

        gross_pl += prof_loss

    #print(Months)

    average_pl = round(((total_pl[85] - total_pl[0]) / 86), 2)

    

    total_months = int(len(Months)) 

    ###average_profits = total_profits / total_months


    max_increase = total_pl[0]
    for i in range(len(total_pl)):
        if max_increase < total_pl[i]:
            max_increase = total_pl[i]
            if max_increase == total_pl[i]:
                high_month = Months[i]
                    
    #print(high_month)

    max_decrease = total_pl[0]
    for i in range(len(total_pl)):
        if max_decrease > total_pl[i]:
            max_decrease = total_pl[i]
            if max_decrease == total_pl[i]:
                low_month = Months[i]

    #print(low_month)

    print("Financial Analysis")

    print("---------------------------------------------")

    print(f"Total Months: {total_months}")

    print(f"Total: ${gross_pl}")

    print(f"Average Change: ${average_pl}")

    print(f"Greatest Increase in Profits: {high_month} (${max_increase})")

    print(f"Greatest Decrease in Profits: {low_month} (${max_decrease})")

    #print(total_pl)

    ###print(average_profits)

output_path = os.path.join("Analysis", "bank_analysis.txt")


with open(output_path, 'w') as txtfile:

    lines = ['Financial Analysis\n', '-------------------------------------------------\n', f"Total Months: {total_months}\n", f"Total: ${gross_pl}\n", f"Average Change: ${average_pl}\n", f"Greatest Increase in Profits: {high_month} (${max_increase})\n", f"Greatest Decrease in Profits: {low_month} (${max_decrease})\n"]

    txtfile.writelines(lines)

    txtfile.close()
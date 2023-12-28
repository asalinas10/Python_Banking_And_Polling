# import modules

import os
import csv

# impor csv file to variable

pybankcsv = os.path.join("Resources", "budget_data.csv")

# create lists for months and toal profits/losses

Months = []

total_pl = []

# open csv file

with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Set header line aside

    csv_header = next(csvfile)

    # set profits/losses counter to 0

    gross_pl = 0


    # append Months, total_pl lists and gross_pl counter

    for row in csvreader:
        Months.append(row[0])

        total_pl.append(int(row[1]))

        prof_loss = int(row[1])

        gross_pl += prof_loss

    # find total months
    total_months = int(len(Months))

    print(total_months) #86

    # find average profit/loss by dividing total_pl over total_months 

    average_pl = round(((total_pl[85] - total_pl[0]) / total_months), 2)

    
    # next section is to find which months had the single greatest increase and decrease in profits from whole data set
    
    # set month_increase to first index of total_pl for starting point

    month_increase = total_pl[0]

    # set loop that checks if month_increase is less than the current index of total_pl

    for i in range(len(total_pl)):
        if month_increase < total_pl[i]:

            # if month_increase is less than total_pl[i] then replace month_increase with total_pl[i] as it is now
            month_increase = total_pl[i]

            # if month_increase is equivalent to total_pl[i] then set high_month to Months[i]

            if month_increase == total_pl[i]:
                high_month = Months[i]
                    

    # set month_decrease to first index of total_pl for starting point

    month_decrease = total_pl[0]

    # set loop that checks if month_decrease is greater than the current index of total_pl

    for i in range(len(total_pl)):
        if month_decrease > total_pl[i]:

            # if month_decrease is greater than total_pl[i] then replace month_decrease with total_pl[i] as it is now
            month_decrease = total_pl[i]

            # if month_decrease is equivalent to total_pl[i] then set low_month to Months[i]

            if month_decrease == total_pl[i]:
                low_month = Months[i]

    

# set up export path for analysis file

output_path = os.path.join("Analysis", "bank_analysis.txt")

# using the export path create a text file with neccesary financial information

with open(output_path, 'w') as txtfile:

    lines = ['Financial Analysis\n', 
             '-------------------------------------------------\n', 
             f"Total Months: {total_months}\n", 
             f"Total: ${gross_pl}\n", 
             f"Average Change: ${average_pl}\n", 
             f"Greatest Increase in Profits: {high_month} (${month_increase})\n", 
             f"Greatest Decrease in Profits: {low_month} (${month_decrease})\n", 
             '-------------------------------------------------\n']

    txtfile.writelines(lines)

    txtfile.close()
#import modules

import os
import csv

# import csv to variable
csvpath = os.path.join('Resources/election_data.csv')

# create ballot_ids list

ballot_ids = []

# open csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # set aside header line in csv file

    csv_header = next(csvreader)
    
    # set vote counters to 0

    total_votes = 0

    charles_votes = 0

    diana_votes = 0

    raymon_votes = 0

    # loop through rows in csv file

    for row in csvreader:

        # append ballot_ids
        ballot_ids.append(row[0])

        # set if statements to count candidate votes

        if row[2] == "Charles Casper Stockham":
            charles_votes += 1

        if row[2] == "Diana DeGette":
            diana_votes += 1

        if row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

    # make loop to count total votes

    for ballots in range(len(ballot_ids)):
        total_votes += 1

    # find percentage of votes each candidate recieved

    charles_p = round(((charles_votes / total_votes) * 100), 2)

    diana_p = round(((diana_votes / total_votes) * 100), 2)

    raymon_p = round(((raymon_votes / total_votes) * 100), 2)

# set output path for analysis text file

output_path = os.path.join("Analysis/poll_results.txt")

# set up text file

with open(output_path, 'w') as txtfile:

    lines = ['Election Results\n', 
             '-------------------------------------------------\n', 
             f"Total Votes: {total_votes}\n", 
             "-------------------------------------------------\n", 
             f"Charles Casper Stockham: {charles_p}% ({charles_votes})\n", 
             f"Diana DeGette: {diana_p}% ({diana_votes})\n", 
             f"Raymon Anthony Doane: {raymon_p}% ({raymon_votes})\n", 
             "-------------------------------------------------\n", 
             "Winner: Diana DeGette\n",
             "-------------------------------------------------\n"]

    txtfile.writelines(lines)

    txtfile.close()
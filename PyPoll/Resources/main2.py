import os
import csv
from pathlib import Path

# Declare file location through pathlib
input_file = Path("python-challenge", "PyPoll", "election_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_votes = []
total_profit = []
monthly_profit_change = []
csvpath = "./Resources/election_data.csv"
candidates_and_votes = {}
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip the header labels to iterate with the values
    header = next(csvreader)
    # Iterate through the rows in the stored file contents
    for row in csvreader:
        total_votes.append(row[0])
        if row[2] in candidates_and_votes:
            candidates_and_votes[row[2]] = candidates_and_votes[row[2]] + 1
        else:
            candidates_and_votes[row[2]] = 1

output_file = "./Analysis/election_data.txt"
with open(output_file,"w") as file:
    
    print("Election Results")
    file.write("Election Results\n")
    print("-------------------------")
    file.write("-------------------------\n")
    print(f"Total Votes: {len(total_votes)}")
    file.write(f"Total Votes: {len(total_votes)}\n")
    print("-------------------------")
    file.write("-------------------------\n")
    winner = next(iter(candidates_and_votes))
    for candidate, votes in candidates_and_votes.items():
        print(f"{candidate}: {100*votes/len(total_votes):.3f}% ({votes})")
        file.write(f"{candidate}: {100*votes/len(total_votes):.3f}% ({votes})\n")
        if votes > candidates_and_votes[winner]:
            winner = candidate
    print("-------------------------")
    file.write("-------------------------\n")
    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}\n")
    print("-------------------------")
    file.write("-------------------------\n")
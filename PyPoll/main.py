## TASKS
    # Total votes cast
    # A complete list of canidates who recieved votes
        # Percentage of vote won and 
        # total votes
    # The winner of the election

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
with open(election_csv) as election:
    election_data = csv.reader(election)
    header = next(election_data)

    total_votes = 0
    candidate_votes = {} #Key is candidate, value is vote count
    candidates = []

    for line in election_data:
        total_votes += 1
        candidate = line[2]

        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

        else:
            candidate_votes[candidate] += 1

#Calculate the percentage of vote won for each candidate and the winner
cand_percentages = {cand: (votes/total_votes)*100 for cand, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)

#print results to terminal window
print("Election Results")
print("---------------------")
print(f'Total Votes: {total_votes}')
print("---------------------")

for candidate in candidates:
    print(f'{candidate}: {cand_percentages[candidate]:.2f}% ({candidate_votes[candidate]})') #.2f% for decimals

print("---------------------")
print(f'Winner: {winner}')

#print results to new text file in Analysis folder
with open("Analysis/electiion_results.txt","w") as er:
    print("Election Results", file=er)
    print("---------------------", file=er)
    print(f'Total Votes: {total_votes}', file=er)
    print("---------------------",file=er)

    for candidate in candidates:
        print(f'{candidate}: {cand_percentages[candidate]:.2f}% ({candidate_votes[candidate]})',file=er)

    print("---------------------", file=er)
    print(f'Winner: {winner}', file=er)


'''
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.
'''

# import functionality
import os
import csv

# access the csv file that has the election data
csvEDfile = os.path.join("Resources", "election_data.csv")

# Set to zero a new variable to count the number of votes
totalVotes = 0
# A complete list of candidates who received votes
allList = [] # Holds a list of unique candidate names by only adding if they aren't already there
# Next 3 lists just hold values of their own name to be counted later
stockhamList = []
deGetteList = []
doaneList = []
winner = [] #stores the candidate with the most votes

# The total number of votes cast
with open(csvEDfile, encoding="utf-8") as file:
    csvReader = csv.reader(file, delimiter = ",")
    header = next(csvReader)
    # Counts the number of rows after skipping the header row.
    for row in csvReader:
        totalVotes += 1
    # for loop adds in a name to the candidate list only if that name is not already in the list
        if row[2] not in allList:
            allList.append(row[2])
    with open(csvEDfile, encoding="utf-8") as file:
        csvReader = csv.reader(file, delimiter = ",")
        next(csvReader)
        # Creates lists with the candidates name repeated to count later to determine their number of votes
        for row in csvReader:
            if row[2] == allList[0]:
               stockhamList.append(row[2])
            if row[2] == allList[1]:
                deGetteList.append(row[2])
            if row[2] == allList[2]:
                doaneList.append(row[2])
# The next 6 values are the total number of votes and percent of votes each candidate received
stockhamVoteCount = int(len(stockhamList))
deGetteVoteCount = int(len(deGetteList))
doaneVoteCount = int(len(doaneList))
stockhamVotePercent = (stockhamVoteCount / totalVotes) * 100
deGetteVotePercent = (deGetteVoteCount / totalVotes) * 100
doaneVotePercent = (doaneVoteCount / totalVotes) * 100

# This code figures out the winner by ensuring they received more votes than both the other candidates and adds their name to the empty winner dictionary above
if stockhamVoteCount > deGetteVoteCount and stockhamVoteCount > doaneVoteCount:
    winner.append(allList[0])
if deGetteVoteCount > stockhamVoteCount and deGetteVoteCount > doaneVoteCount:
    winner.append(allList[1])
if doaneVoteCount > deGetteVoteCount and doaneVoteCount > stockhamVoteCount:
    winner.append(allList[2])

# prints all the values determined so far to validate
# print(totalVotes) 
# print(allList) 
# print(stockhamVoteCount) 
# print(deGetteVoteCount) 
# print(doaneVoteCount) 
# print(stockhamVotePercent) 
# print(deGetteVotePercent) 
# print(doaneVotePercent) 
# print(winner)

# This creates goes to a new folder to write the findings to an analysis file. 
analysisPath = os.path.join("Analysis", "Election Results.txt") 

with open(analysisPath, 'w') as file:

    # this formats the text to appear as directed in the HW example. 
    file.write(f"Election Results \n-------------------------\nTotal Votes: {totalVotes} \n-------------------------\n{allList[0]}: {stockhamVotePercent:.3f}% ({stockhamVoteCount})\n{allList[1]}: {deGetteVotePercent:.3f}% ({deGetteVoteCount})\n{allList[2]}: {doaneVotePercent:.3f}% ({doaneVoteCount})\n-------------------------\nWinner: {winner[0]}\n-------------------------") 
    file.close()

# Prints the same output to the terminal that is generated in a text file above. 
print(" ")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")
print((allList[0]) + ": " + format(stockhamVotePercent, ".3f") + "% (" + str(stockhamVoteCount) + ")")
print((allList[1]) + ": " + format(deGetteVotePercent, ".3f") + "% (" + str(deGetteVoteCount) + ")")
print((allList[2]) + ": " + format(doaneVotePercent, ".3f") + "% (" + str(doaneVoteCount) + ")")
print("-------------------------")
print("Winner: " + (winner[0]))
print("-------------------------")

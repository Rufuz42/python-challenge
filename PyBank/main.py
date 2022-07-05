'''
    The total number of months included in the dataset #DONE


    The net total amount of "Profit/Losses" over the entire period #DONE


    The changes in "Profit/Losses" over the entire period, and then the average of those changes #DONE


    The greatest increase in profits (date and amount) over the entire period


    The greatest decrease in profits (date and amount) over the entire period   
 '''

# import functionality
import os
import csv

# access the csv file that has the budget data
csvBDfile = os.path.join("Resources", "budget_data.csv")

# holds total months
totalMonths = 0
# calculate net profits (losses) using an accumulator
netProfit = 0
# Changes in profits / losses over the period, then the average of those changes
changeValue = 0
lastValue = 0
totalChange = [] #empty list to store changed values in
monthsOfData = [] #empty list to store months in

# calculate the number of months in the dataset after skipping the header row
with open(csvBDfile, 'r') as file:
    csvReader = csv.reader(file, delimiter = ",")
    header = next(csvReader) # next function skips the header row
    # For loop counts the number of rows remaining, adds to totalMonths. Calculates net profit by adding each value to the previous total.
    # Calculates change in profit by subtracting previous profit value from current, then stores current as the previous value. Along the way,
    # the loop appends the values to an empty list above to be referenced later. 
    for row in csvReader:
        totalMonths += 1
        netProfit += int(row[1])
        dataMonthAndYear = row[0]
        changeValue = int(row[1]) - lastValue
        lastValue = int(row[1]) # calculates this last to store it for the next for loop iteration
        totalChange.append(changeValue) # adds data to the empty list above
        monthsOfData.append(dataMonthAndYear) # adds month and year to a list
totalChange.pop(0) # removes the first value from the list, list should start with 2nd value minus first
# print(totalChange)
# print(monthsOfData)
# Calculates the average change by summing them all up and dividing by the number of items summed.
averageValue = (sum(totalChange) / len(totalChange))
# print(averageValue)

# will hold month and value of greatest increase / decrease
greatestIncrease = [monthsOfData[0], totalChange[0]] 
greatestDecrease = [monthsOfData[0], totalChange[0]]

# Use this loop to calculate the index of the greatest increase and decrease value
for month in range(len(totalChange)):
    if(totalChange[month] > greatestIncrease[1]):
        # If true, this value becomes the new greatest increase
        greatestIncrease[1] = totalChange[month]
        # Update the month and year as well, have to use + 1 since I popped the first list values
        greatestIncrease[0] = monthsOfData[month + 1]

    if(totalChange[month] < greatestDecrease[1]):
        # If true, this value becomes the new greatest decrease
        greatestDecrease[1] = totalChange[month]
        # Update the month and year as well, have to use + 1 since I popped the first list values
        greatestDecrease[0] = monthsOfData[month + 1]
# print(greatestIncrease[0])
# print(greatestIncrease[1])
# print(greatestDecrease[0])
# print(greatestDecrease[1])

# This creates goes to a new folder to write the findings to an analysis file. 
analysisPath = os.path.join("Analysis", "Financial Analysis.txt") 

with open(analysisPath, 'w') as file:

    # this formats the text to appear as directed in the HW example. 
    file.write(f"Financial Analysis \n----------------------------\nTotal Months: {totalMonths}\nTotal: ${netProfit}\nAverage Change: ${averageValue:.2f}\nGreatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\nGreatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")
    file.close()

# Prints the same output to the terminal that is generated in a text file above. 
print(" ")
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(totalMonths))
# print("Average Change: $" + format(averageValue, ".2f"))
print(f"Average Change: ${averageValue:.2f}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")

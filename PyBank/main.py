## TASK
    # Total number of months included in the dataset -- count line[0]
    # the net total amount of "Profit/losses" over the entire period -- sum line[1]
    # The changes in "profit/losses" over the entire period, and then the average of the changes -- delta lines[] avg delta lines[]
    # The greatest increase in profits (date and amount) over the entire period -- max line[1] print line[0], line[1]
    # The greatest decrease in profits (date and amount) over the entire period -- min line[1] print line[0], line[1]

    # Print the analysis to the terminal and export a text file with the results


import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as budget_file:
    csvreader = csv.reader(budget_file)
    header = next(csvreader)

    delta_lines = []
    total_months = 0
    monthly_change = {} #Key is month value is profit change
    past_profit = 0
    total_profit = 0

    for line in csvreader:
        total_months += 1
        month = line[0]
        profit = int(line[1]) 
        total_profit += profit

        if past_profit != 0: 
            change = profit - past_profit ## other way around? 
            delta_lines.append(change)
            monthly_change[month] = change
        past_profit = profit
avg_change = sum(delta_lines)/len(delta_lines) 
max_increase = max(delta_lines) ## figure out how to print the months with it
max_loss = min(delta_lines) ## use different variable name? 
month_max_increase = [key for key, value in monthly_change.items() if value == max_increase][0] #to show just the key in the dictiorary associated with highest value
month_max_loss = [key for key, value in monthly_change.items() if value == max_loss][0]

print("Financial Analysis")
print('___________________________________')
print(f'Total months: {total_months}')
print(f'total: ${total_profit}')
print(f"Average Change: ${avg_change:.2f}") ##.2f for decimals
print(f"Greatest increase in profits: {month_max_increase} (${max_increase})") ## need to add the month 
print(f"Greatest Decrease in profits: {month_max_loss} (${max_loss})")


with open("Analysis/budget_analysis.txt", 'w') as af:

    print("Financial Analysis", file=af)
    print('___________________________________', file=af)
    print(f'Total months: {total_months}', file=af)
    print(f'total: ${total_profit}', file=af)
    print(f"Average Change: ${avg_change:.2f}", file=af) ##.2f for decimals
    print(f"Greatest increase in profits: {month_max_increase} (${max_increase})", file=af) ## need to add the month 
    print(f"Greatest Decrease in profits: {month_max_loss} (${max_loss})", file=af)










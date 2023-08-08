import csv
import os

# create the path
csvpath = os.path.join("Resources", "budget_data.csv")
# print(csvpath)

# open the path
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader) #skips data on row 1 (the header row) and stores it in 'csv_header'
    # print(f"CSV Header: {csv_header}")
    firstrow = next(csvreader) # skips data on row 2 and stores it in 'firstrow'

    #counters!
    monthscounter = 0 
    totalprofit = 0 
    #changeslist = [] # list of changes in profit/losses
    totalchange = 0
    prev_row = int(firstrow[1])  # telling Python that 'prev_row' is row 2 data that we skipped and stored in 'prev_row'
    maxprofit = 0
    minprofit = 0
    maxprofit_month = [""]
    minprofit_month = [""]

    #for loop to read through document row by row
    for rows in csvreader:
        monthscounter += 1 # sum of the number of months
        totalprofit += prev_row # sum of profits/losses column --- print(type(rows[1])) ... to check what datatype 'rows' is in the csv file (they look like integers because they're numbers, but they're actually strings!
        #changeslist.append(rows[1]) # add values to the totalchanges list
        change = int(rows[1]) - prev_row # calculates each month's pnl change
        prev_row = int(rows[1]) # resetting the value of each row before next pnl change calculation
        totalchange += change # sum of all changes

        if change > maxprofit:
            maxprofit = change
            maxprofit_month = rows[0]
        
        if change < minprofit:
            minprofit = change
            minprofit_month = rows[0]

    #print(monthscounter + 1)
    #print(f"${totalprofit + int(rows[1])}")
    #print(totalchange / monthscounter)
    #print(f'{maxprofit_month} (${maxprofit})')
    #print(f'{minprofit_month} (${minprofit})')

output = f"""
Financial Analysis
-----------------------------------------
Total Months: {monthscounter + 1}
Total: ${totalprofit + int(rows[1])}
Average Change: ${totalchange / monthscounter:.2f}
Greatest Increase in Profits: {maxprofit_month} (${maxprofit})
Greatest Decrease in Profits: {minprofit_month} (${minprofit})
"""
print(output)


file = 'Analysis/output_file.txt'
with open(file, 'w') as textfile:
    #print(text)
    textfile.write(output)
    #print(lines)


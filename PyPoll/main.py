import csv
import os

# set the path to locate csv
csvpath = os.path.join("Resources", "election_data.csv")
#print(csvpath)

# open the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skips data on row 1 (the header row) and stores it in 'csv_header' variable

    # counters! 
    totalvotes = 0
    Stockham_votes = 0
    Degette_votes = 0
    Doane_votes = 0

    # other variables to store data
    Stockham_name = "Charles Casper Stockham"
    Degette_name = "Diana DeGette"
    Doane_name = "Raymon Anthony Doane"
    
    # for loop to read through csv file row by row
    for rows in csvreader:
        totalvotes += 1
        
        # if statement to find values containing candidate names
        if rows[2] == Stockham_name:
            Stockham_votes += 1
    
        elif rows[2] == Degette_name:
            Degette_votes += 1
    
        elif rows[2] == Doane_name:
            Doane_votes += 1
           
    # calculating each candidate percentage of total votes
    Stockham_percent = (Stockham_votes/totalvotes)*100    
    Degette_percent = (Degette_votes/totalvotes)*100
    Doane_percent = (Doane_votes/totalvotes)*100

    # dictionary to link corresponding key (percent variables) to value (candidate name)
    candidate_percent = {
        (Stockham_percent): Stockham_name, 
        (Degette_percent): Degette_name, 
        (Doane_percent): Doane_name
    }
    # new variable to store max value and corresponding key from dictionary, to locate the winner!
    winner = (candidate_percent.get(max(candidate_percent)))



output = f"""
Election Results
----------------------
Total Votes: {totalvotes}
----------------------
Charles Casper Stockham: %{Stockham_percent:.3f} ({Stockham_votes})
Diana DeGette: %{Degette_percent:.3f} ({Degette_votes})
Raymon Anthony Doane: %{Doane_percent:.3f} ({Doane_votes})
----------------------
Winner: {winner}
"""


file = 'Analysis/output_file.txt'
with open(file, 'w') as textfile:
    textfile.write(output)


# ---------------------------------------------------------
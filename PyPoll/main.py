# import modules
import os
import csv

# set path for file
csv_file_path = os.path.join("C:/Users/mbocc/COLNYC20190716DATA/02-Homeworks/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Open the CSV
with open(csv_file_path, newline="") as csv_file:
    csv_header = next(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=",")
    poll = []
    
    i = 0
    for row in csv_reader:
        poll.append(int(row[0])) 
        i = i + 1
    csv_file.seek(0)

#count votes
    k = 0
    c = 0
    l = 0
    o = 0
    
    for row in csv_reader:
        vote = row[2]
        if (vote == "Khan"):   
            k = k + 1
        elif (vote == "Correy"):
            c = c + 1
        elif (vote == "Li"):
            l = l + 1
        elif (vote == "O'Tooley"):
            o = o + 1

#define winner            
    winner = max(k ,c, l, o)
    if k > c and k > l and k > o:
        winner_name = "Khan"
    elif c > k and c > l and c > o:
        winner_name = "Correy"
    elif l > c and l > k and l > o:
        winner_name = "Li"
    elif o > c and o > l and o > k:
        winner_name = "O'Tooley"

#vote percentages
    sum = k + c + l + o
    k_percentage = round((k / sum *100),0)
    c_percentage = round((c / sum *100),0)
    l_percentage = round((l / sum *100),0)
    o_percentage = round((o / sum *100),0)

#print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(i))
print("-------------------------")
print("Khan: " + str(k_percentage) + "(" + str(k) + ")") 
print("Correy: " + str(c_percentage) + "(" + str(c) + ")")
print("Li: " + str(l_percentage) + "(" + str(l) + ")")
print("O'Tooley: " + str(o_percentage) + "(" + str(o) + ")")
print("-------------------------")
print("Winner: " + str(winner_name))
print("-------------------------")

#export file
export_file = 'results.txt' 
with open(export_file, 'w') as textfile: 
    textfile.write("Election Results")
    x = ("----------------------------",
    "\n",
    f'Total Votes: {i}\n',
    "----------------------------\n",
    f'Khan: {k_percentage}% ({k})\n',
    f'Correy: {c_percentage}% ({c})\n',
    f'Li: {l_percentage}% ({l})\n',
    f'OTooley: {o_percentage}% ({o})\n',
    "----------------------------\n",
    f'Winner: {winner_name}\n',
    "----------------------------\n")
    textfile.writelines(x)
    textfile.close()
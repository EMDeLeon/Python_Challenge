import os
import csv

#Variables

totalvotes=0
name_list=[]
candidate_name=[]


vote_counter= [0,0,0,0]
vote_percent= [0,0,0,0]
winner =[] 


csvpath= os.path.join ("..", "PyPoll","election_data.csv")
with open (csvpath, "r", newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
   
    #skipping the header row
    csv_header= next(csvreader) 
   #count total votes by counting the rows in row zero & list of candidates 
    for row in csvreader: 
            totalvotes += 1
            name_list.append(str(row[2]))
    for row[2] in name_list:
            if row[2] not in candidate_name:
                candidate_name.append(row[2])
            if row[2] == candidate_name[0]:
                vote_counter[0] += 1
            elif row[2] == candidate_name[1]:
                vote_counter[1] += 1
            elif row[2] == candidate_name[2]:
                vote_counter[2] += 1
            elif row[2] == candidate_name[3]:
                vote_counter[3] += 1
    
# create a function to calculate the percentage of the total vote for each candidate
    
    vote_percent[0] = round(100 * (vote_counter[0] / totalvotes), 4)
    vote_percent[1] = round(100 * (vote_counter[1] / totalvotes), 4)
    vote_percent[2] = round(100 * (vote_counter[2] / totalvotes), 4)
    vote_percent[3] = round(100 * (vote_counter[3] / totalvotes), 4)
    
# Determine who the winner is by identifying the max vote count within total votes for each candidate
    if vote_counter[0] == max(vote_counter[0], vote_counter[1], vote_counter[2], vote_counter[3]):
        winner = candidate_name[0]
    elif vote_counter[1] == max(vote_counter[0], vote_counter[1], vote_counter[2], vote_counter[3]):
        winner = candidate_name[1]
    elif vote_counter[2] == max(vote_counter[0], vote_counter[1], vote_counter[2], vote_counter[3]):
        winner = candidate_name[2]
    elif vote_counter[3] == max(vote_counter[0], vote_counter[1], vote_counter[2], vote_counter[3]):
        winner = candidate_name[3]



# print the report to the terminal screen
    
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------------")
print(f"{candidate_name[0]}: {vote_percent[0]}% ({vote_counter[0]})")
print(f"{candidate_name[1]}: {vote_percent[1]}% ({vote_counter[1]})")
print(f"{candidate_name[2]}: {vote_percent[2]}% ({vote_counter[2]})")
print(f"{candidate_name[3]}: {vote_percent[3]}% ({vote_counter[3]})")
print("-----------------------------")
print(f"Winner: {winner}")

#output Files 
file= open("file.txt","w")
file.write("Election Results\n")
file.write("--------------------------------------------\n")
file.write("Total Votes:\n" + str(totalvotes))
file.write("--------------------------------------------\n")
file.write("{candidate_name[0]}: {vote_percent[0]}% ({vote_counter[0]})")
file.write("{candidate_name[1]}: {vote_percent[1]}% ({vote_counter[1]})")
file.write("{candidate_name[2]}: {vote_percent[2]}% ({vote_counter[2]})")
file.write("{candidate_name[3]}: {vote_percent[3]}% ({vote_counter[3]})")
file.write("--------------------------------------------\n")
file.write("Winner:\n" + str(winner))

file.close()
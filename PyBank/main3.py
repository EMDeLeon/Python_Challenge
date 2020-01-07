
import os
import csv

#Variables 
Ttl_months = 0
Ttl_profit_loss = 0
profit_loss=0
avg_profitLoss= 0
greatest_increase_date = ''
greatest_increase_value = 0
greatest_decrease_date = ''
greatest_decrease_value = 0
prev_profit_loss= 0
profit_chg_list=[]


  
#Calling on the file needed to open
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
with open (csvpath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
 
#Total Number of Months
    #skipping the header row
    csv_header= next(csvreader) 
    
    #Loop 
    for row in csvreader: 
#The total number of months included in the dataset
        cell_date= row[0] 
        if(cell_date): 
            Ttl_months = Ttl_months + 1
            
#The net total amount of "Profit/Losses" over the entire period
        profit_loss= int(row[1])
        if(profit_loss):
            Ttl_profit_loss= Ttl_profit_loss + profit_loss
   
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period          
        profit_change= profit_loss- prev_profit_loss
        if profit_change >= 0:
            if profit_change > greatest_increase_value:
                greatest_increase_date= cell_date 
                greatest_increase_value = profit_change 
                
        else:
            if profit_change < greatest_decrease_value:
                greatest_decrease_date= cell_date
                greatest_decrease_value = profit_change
            
            prev_profit_loss = profit_loss 
           
#The average of the changes in "Profit/Losses" over the entire period
        prev_profit_loss = profit_loss 
        profit_chg_list.append(profit_change)

profit_chg_list[0]=0
for value in range(len(profit_chg_list)):
    if value == 0:
        Ttl_profit_loss += 0
        
    else:
        Ttl_profit_loss += profit_chg_list[value] - profit_chg_list[value - 2]
        avg_profitloss = sum(profit_chg_list)/(len(profit_chg_list)-1)
        
        
                   
#Print each output 
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {Ttl_months}")
print(f"Total: ${Ttl_profit_loss}")
print(f"Average Change: ${avg_profitloss}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})")

#output Files 
outputfile= open("outputfile.txt","w")

outputfile.write("Financial Analysis\n")

outputfile.write("--------------------------------------------\n")

outputfile.write("Total Number of Months:\n" + str(Ttl_months))

outputfile.write("Total Profit/Loss:" +str(Ttl_profit_loss))

#outputfile.write("Average Change:" +str(avg_profitloss))

outputfile.write("Greatest Increase Date:" + str(greatest_increase_date))

outputfile.write("Greatest Increase Value:" + str(greatest_increase_value))

outputfile.write("Greatest Decrease Date:" + str(greatest_decrease_date))

outputfile.write("Greatest Decrease Date:" + str(greatest_decrease_value)) 


outputfile.close()
                  


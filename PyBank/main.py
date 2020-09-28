#import os module
import os

#import csv module for opening csv files, set path for csv file
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#open csv file and tell python to read data in file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header row and go straight to the data
    header = next(csvreader)

    #set initial values for variables
    month_count = 0
    pl_total = 0
    mean = 0 
    pl_change_list = []
    past_pl = 867884
    pl_change = 0
    max_gain = ["", pl_change]
    min_loss = ["", pl_change]
            
    #read each value in the row and calculate the following
    for row in csvreader:        
        #calculate the month counter by adding one for each iteration
        month_count += 1
        #calculate the total profit/loss continuing to add the value from column 1 
        pl_total = pl_total + int(row[1])
        #calculate the change in profit/loss from row to row by subtracting the last row's value
        pl_change = int(row[1]) - past_pl
        #reset the past profit/loss value to be the current row's column 1 value
        past_pl = int(row[1])
        #add the value of the profit/loss change to the change list
        pl_change_list.append(pl_change)
 
        #calculate the greatest increase in profit
        if(pl_change > max_gain[1]):
            max_gain[0]=row[0]
            max_gain[1]=pl_change
        #calculate the greatest decrease in losses
        if(pl_change < min_loss[1]):
            min_loss[0]=row[0]
            min_loss[1]=pl_change
    
    #calculate the sum of the profit/loss change list
    sum_pl_change = sum(pl_change_list)
    #calculate the average of the profit/loss changes
    mean_pl_change = "{:.2f}".format(sum_pl_change/(len(pl_change_list)-1))
    
    #print the final values for the user to see
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Number of Months: {month_count}")
    print(f'Net Total Profit/Loss: ${pl_total}')
    print(f'Average Change in Profit/Loss: ${mean_pl_change}')
    print(f'Greatest Increase in Proft: {max_gain[0]} (${max_gain[1]})')
    print(f'Greatest Decrease in Profit: {min_loss[0]} (${min_loss[1]})')
    
    #export same results to text file
    import sys
    file = open('results.txt', 'a')
    sys.stdout = file
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Number of Months: {month_count}")
    print(f'Net Total Profit/Loss: ${pl_total}')
    print(f'Average Change in Profit/Loss: ${mean_pl_change}')
    print(f'Greatest Increase in Proft: {max_gain[0]} (${max_gain[1]})')
    print(f'Greatest Decrease in Profit: {min_loss[0]} (${min_loss[1]})')
    file.close()
    #export text file with results
     
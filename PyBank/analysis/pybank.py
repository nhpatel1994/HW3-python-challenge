import os
import csv

total_profit_loss = 0
current = 0
last = 0

total_change = 0
months = 0

greatest_increase = 0
greatest_decrease = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #Loop through every row in the csv file
    for row in csvreader:

         #Keep a running total of profit
        total_profit_loss = total_profit_loss + int(row[1])
        
        #Keep a running total of the number of months
        months = months + 1

        current = int(row[1])

        if months > 1:

            #Determine the difference between current month and previous months earnings
            change = current - last

            #Determine if current month had the greatest increase from previous month, then store that value.
            if  greatest_increase < change:
                greatest_increase = change
                greatest_increase_date = str(row[0])

            #Determine if current month had the greatest decrease from previous month, then store that value.
            if  greatest_decrease > change:
                greatest_decrease = change
                greatest_decrease_date = str(row[0])


            #Keep a running total of overall change
            total_change = total_change + change
            average_change = total_change / (months-1)
            format_average_change = "{:.2f}".format(average_change)

        #set last to be the current row to be used for next iteration
        last = int(row[1])

print ("Total Months: ", months)
print ("Total: $",total_profit_loss)
print ("Average Change: $",format_average_change)
print ("Greatest Increase in Profits: ",greatest_increase_date, "( $" , greatest_increase, ")")
print ("Greatest Decrease in Profits: ", greatest_decrease_date, "( $" , greatest_decrease, ")")

with open("pybank.txt", "w") as txt_file:

    output = "---------------------------------------------------"
    txt_file.write(output + '\n')
    output = "Total Months: " + str(months)
    txt_file.write(output + '\n')
    output = "Total: $" + str(total_profit_loss)
    txt_file.write(output + '\n')
    output = "Average Change: $" + str(format_average_change)
    txt_file.write(output + '\n')
    output = "Greatest Increase in Profits: " + str(greatest_increase_date) + "( $" + str(greatest_increase) + ")"
    txt_file.write(output + '\n')
    output = "Greatest Decrease in Profits: " + str(greatest_decrease_date) + "( $" + str(greatest_decrease) + ")"
    txt_file.write(output + '\n')
    output = "---------------------------------------------------"
    txt_file.write(output + '\n')
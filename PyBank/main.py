#importing os to create dynamic path to external files
import os
import csv

#attaching budget data to main.py
#file_to_load = os.path.join(".", "Resources", "budget_data.csv")
#file_to_output = os.path.join(".", "budget_analysis.txt")

current_directory = os.path.dirname(os.path.abspath(__file__)) 
file_to_load = os.path.join(current_directory, "Resources", "budget_data.csv")   
current_directory_output = os.path.dirname(os.path.abspath(__file__)) 
file_to_output = os.path.join(current_directory_output, "analysis", "budget_analysis.txt")

total_months = 1
net = 0
net_change_list = []
greatest = ["", 0]
least = ["", 99999999909999999999]

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # print(reader)

    #header row
    header = next(reader)
    #print(header)

    #first row of data and net
    data_row = next(reader)
    #print(data_row[1]) #grabing just the number and not the whole next row
    net = net + int(data_row[1])
    prev_net = int(data_row[1])

    #months, net total
    for row in reader:
        total_months += 1
        net += int(row[1])
        
        #change of net
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        net_monthly_avg = sum(net_change_list)/ len(net_change_list)

        if(net_change > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = net_change
        
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change

#print(net_change_list)
#print(greatest)
#print(least)

output = (
    f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net}\n"
    f"Average Change: ${net_monthly_avg: .2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})"
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
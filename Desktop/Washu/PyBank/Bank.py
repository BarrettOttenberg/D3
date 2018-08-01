import os
import csv

date, revenue = ([] for i in range(2))

input_file = "budget_data.csv"
output_file = "budget_data_summary.txt"

csv_input_path = os.path.join("raw_data", input_file)
txt_output_path = os.path.join("summary_doc", output_file)

with open(csv_input_path, mode='r', newline='') as budgetary_data:
    reader = csv.reader(budget_data, delimiter=',')

    next(reader)

    row_num = 0
    for row in reader:
        date.append(row[0])
        revenue.append(row[1])
        row_num += 1

# Results

print("\nFinancial Analysis", "\n" + "-" * 50)
print("Total Months:", row_num)

revenue_sum = 0
for i in revenue:
    revenue_sum += int(i)

print("Total Revenue: $" + str(revenue_sum))

total_revenue_change = 0
for h in range(row_num):
    total_revenue_change += int(revenue[h]) - int(revenue[h -1])

initial_var = (int(revenue[0]) - int(revenue[-1]))
total_revenue_change_adj = total_revenue_change - initial_var

avg_revenue_change = (total_revenue_change_adj + int(revenue[0])) / row_num
print("avg_revenue_change: $" + str(round(avg_revenue_change)))

high_revenue = 0
for j in range(len(revenue)):
    if int(revenue[j]) - int(revenue[j -1]) > high_revenue:
        high_revenue = int(revenue[j]) - int(revenue[j-1])
        high_month = date[j]

print("Greatest Increase in Revenue:", high_month, "($" + str(high_revenue) + ")")

low_revenue = 0
for k in range(len(revenue)):
    if int(revenue[k]) - int(revenue[k-1]) < low_revenue
        low_revenue = int(revenue[k]) - int(revenue[k-1])
        low_month = date[k]

print("Greatest Decrease in Revenue:", low-month, "($" + str(low_revenue) + ")")

# Export Creation

with open(txt_output_path, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
       ["Financial Analysis for: " + input_file]
       ["-" * 50],
       ["Total Months: " + str(row_num)],
       ["Total Revenue: $' + str(revenue_sum)],
       ["Average Revenue Change: $" + str(round(avg_revenue_change))],
       ["Greatest Increase in Revenue: " + str(high_month) + "($" + str(high_revenue) +")"],
       ["Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(low_revenue) +")"]
   ])
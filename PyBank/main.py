import os
import csv

date = []
profit_loss = []

month_count = 0
net_total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
average_change = 0

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
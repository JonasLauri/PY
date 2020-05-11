import csv
import os

with open('Per the International Monetary Fund (2019 estimates).csv', 'r') as  csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_tables.csv', 'w') as new_file:
        headers = [
            "Country/Territory",
            "GDP(US$million)",
            "Rank"
        ]
        csv_writer = csv.DictWriter(new_file, headers, delimiter=';')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
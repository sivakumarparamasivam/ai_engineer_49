import csv


with open('data.csv', mode='a+', newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['I', 'am', 'fine', 'thank', 'you'])
    csv_writer.writerows([['I', 'am', 'fine', 'thank', 'you'], ['I', 'am', 'fine', 'thank', 'you']])

with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row[0].ljust(15), row[1].ljust(15), row[2].ljust(15), row[3].ljust(15), row[4].ljust(15))


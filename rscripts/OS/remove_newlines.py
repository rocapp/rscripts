import csv

input_file = input("enter input file path")
output_file = input("enter output file path")

if '.csv' not in input_file:
	input_file = input_file + '.csv'

if '.csv' not in output_file:
	output_file = output_file + '.csv'

out = list()

with open(input_file, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print(row)
		if len(row) > 0:
			out.append(row)
# Output
with open(output_file, 'w+', newline='') as csvnew:
	spamwriter = csv.writer(csvnew, delimiter=',')
	for o in out:
		spamwriter.writerow(o)
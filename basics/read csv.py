#Practice reading in a csv file and extracting the data

import csv

with open('data.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are {", ".join(row)}')
            line_count+=1
        else:
            print(f'\tCharacter details: {row[0]} | {row[1]} | {row[2]} | {row[3]}')
            line_count+=1
    print(f'Processed {line_count} lines')

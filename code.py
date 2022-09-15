""" scriptTitles
Usage:
    scriptTitles  <original_file_name.dat> <original_file_name2.dat> <report_file.dat> 
"""
#!/usr/bin/env python3

import csv
from docopt import docopt

args = docopt(__doc__)

with open(args['<original_file_name.dat>'], 'r', encoding='utf8') as file_input, open(args['<original_file_name2.dat>'], 'r', encoding='utf8') as file_input2, open(args['<report_file.dat>'], 'w', encoding='utf8') as report_file :    
    writer = csv.writer(report_file, delimiter=',') 
    reader = csv.DictReader(file_input, delimiter=',')
    reader2 = csv.DictReader(file_input2, delimiter=',')

    writer.writerow(['Handle','Title','Body (HTML)'])
    
    for row in reader:
        #for i in row[0]:  
            #print(i) 
        handle = row['Handle']
        title = row['Title']
        body = row['Body (HTML)']
            # Adicionar todas as variáveis da coluna 

    writer.writerow([handle , title , body])
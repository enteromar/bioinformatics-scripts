import pandas as pd
import sys
import numpy

column_a = 'isolation_source'
column_b = 'collection_date'
column_c = 'isolation_source'
csv_file_a=str(sys.argv[1])
out_filename=str(sys.argv[2])
dataset = pd.read_csv(csv_file_a)
#dataset_column=dataset[column_a]
print dataset
print 'filtering by',column_a,'...'
indexes=[]
wordlist=['nan','NaN','Nan','NAN','None']
for index, row in dataset.iterrows():
	if str(row[column_a]) not in wordlist and str(row[column_b]) not in wordlist and str(row[column_c]) not in wordlist:
		 print row[column_a],index
		 indexes.append(index)
#save rows by indexes
print 'number of filtered genomes:',len(indexes)
filtered = dataset.ix[indexes]

savefile=pd.io.formats.format.CSVFormatter(filtered,out_filename)
savefile.save()
print 'filtered files saved... as',out_filename


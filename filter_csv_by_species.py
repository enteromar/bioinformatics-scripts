import pandas as pd
import sys
import numpy

column_d = 'scientific_name'
csv_file_a=str(sys.argv[1])
out_filename=str(sys.argv[2])
dataset = pd.read_csv(csv_file_a)

print 'filtering by',column_d,'...'
indexes=[]
species=[
'faecium',
'faecalis',
'hirae',
'mundtii',
'durans',
'avium',
'casseliflavus',
'gallinarum']
for index, row in dataset.iterrows():
	name=str(row[column_d]).split(" ")
	if  len([i for e in species for i in name if e in i]) > 0:
		 indexes.append(index)
	else:
		print row[column_d],index
#save rows by indexes
print 'number of filtered genomes:',len(indexes)
filtered = dataset.ix[indexes]
savefile=pd.io.formats.format.CSVFormatter(filtered,out_filename)
savefile.save()
print 'filtered files saved... as',out_filename


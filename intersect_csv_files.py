import pandas as pd
import sys

csv_b_column_itens=[]
file_a=str(sys.argv[1])
file_b=str(sys.argv[2])


fields=[
'country',
'strain',
'isolation_source',
'organism']

def contains_id(id):
	result=False
	for row in csv_b_column_itens:
		if id in row:
			result=True
	return result 

def intersection():
	#save rows by indexes
	dataset_intersection = dataset_a.ix[indexes_a]
	out_filename='genomes_intersection_EMBL_NCBI.csv'
	savefile=pd.io.formats.format.CSVFormatter(dataset_intersection,out_filename)
	savefile.save()
	print 'intersection of files saved... at',out_filename

def difference(dataset,indexes):
	
	all_indexes = dataset.index.tolist()
	#get difference from the two sets
	diff_index = set(all_indexes) - set(indexes)
	
	dataset_diff = dataset_a.ix[diff_index]

	out_filename = 'genomes_diff_EMBL_NCBI.csv'
	savefile=pd.io.formats.format.CSVFormatter(dataset_diff,out_filename)
	savefile.save()
	print 'diference of files saved... at',out_filename	

def hasEqualsColumns(row_a,row_b):
	return row_a[fields[0]] == row_b[fields[0]] and row_a[fields[1]] == row_b[fields[1]] and row_a[fields[2]] == row_b[fields[2]] and row_a[fields[3]] == row_b[fields[3]]  
	




print 'opening files...'
dataset_a = pd.read_csv(file_a)
dataset_b = pd.read_csv(file_b)

indexes_a=set()
indexes_b=[]
# get indexes of intersection ids
print 'getting intersection of indexes...'
for index_a, row_a in dataset_a.iterrows():
	for index_b, row_b in dataset_b.iterrows():
		if hasEqualsColumns(row_a,row_b):
			indexes_a.add(index_a)
			print index_a

indexes_a=list(indexes_a)
print '\nintersected:\n',len(indexes_a)
#save intersectiond
intersection()
#save differenbce A - B dataset
difference(dataset_a,indexes_a)

from Bio import SeqIO
import sys
import csv
import numpy as np
import glob


def add_features(feature_names,src_features,filename):
	''' return features from a gbff file based on feature_names  '''
	features_data=[]
	v=''
	for i in features_names:
		try:
			v=src_features.qualifiers[i][0]
		except Exception as e:
			v='None'
			#print e,'not finded'
		features_data.append(v)
	#adds filename data in the filename column (last position)	
	features_data[-1]=filename
	return features_data


def get_files():
	''' return a list of files from a specific dir '''
	files = glob.glob("out_genomes/*.gbff")
	#print files
	return files



#features to be extracted from annotation file(gbff) 
features_names=[
'organism',
'mol_type',
'strain',
'isolation_source',
'host',
'db_xref',
'country',
'collection_date',
'filename']


# adds header to csv file
csv_file="genomes_information.csv"
f = open(csv_file, "wb")
writer = csv.writer(f)
entries = [features_names]
writer.writerows(entries)


#process files
files = get_files()
nf=len(files)
i=1
for file in files:
	print 'processing files...',i,'/',nf
	for record in  SeqIO.parse(file, "genbank"):
		src_features = record.features[0]
		features_data=add_features(features_names,src_features,file)
		writer.writerows([features_data])
		break
	i+=1	
f.close()
print 'features saved at',csv_file
print 'finished!'

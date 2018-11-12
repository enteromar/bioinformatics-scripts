import csv
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


with open('P8-1_rep9_plasmid.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    count=1
    sequences=[]
    for row in spamreader:
        if(len(row[1])>1):
            record = SeqRecord(Seq(row[1],
                       IUPAC.protein),
                   id=str(count), name=row[0],
                   description=row[0]+"|" + row[2])
            print record
            sequences.append(record)
        count=count+1
    SeqIO.write(sequences, "rep_09.fasta", "fasta")

import os
import glob
import pandas as pd
#wget -c ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/008/865/GCF_000008865.1_ASM886v1/GCF_000008865.1_ASM886v1_genomic.gbff.gz -O teste.gbff.gz ; gunzip -f teste.gbff.gz

out_dir='out_genomes'
gb_header='GenBank FTP'
rf_header='RefSeq FTP'

def compose_name_file_download(ftp_path,type_file='genbank'):
    """type_file = 'genbank' or 'fasta'"""
    line_split = ftp_path.split("/")
    id_genome = line_split[-1]
    
    if type_file == "genbank":
        compose = ftp_path + "/" + id_genome + "_genomic.gbff.gz"
    elif type_file == "fasta":
        compose = ftp_path + "/" + id_genome + "_genomic.fna.gz"
    else:
        None
        
    return compose


def create_dir(out_dir):
	if not os.path.exists(out_dir):
		print 'creating',out_dir,'directory...'
		os.makedirs(out_dir)


def get_files():
	files = glob.glob("csvs/*.csv")
	#print files
	return files


def download(url,out_dir):
	"""download sequences with wget by url'"""
	try:
		os.system("wget -c --tries=100 " + str(url) + " -P "+out_dir+"/")
	except Exception as e:
		print "download error:",e
    

def main(type_file,out_dir):
	create_dir(out_dir)
	for filename in get_files():	
		print 'reading file',filename,'...\n\n'
		csv = pd.read_csv(filename)
		ftp_column = csv[rf_header]
		print 'downloading files...\n\n'
		for ftp_path in ftp_column:
			if type(ftp_path) is str:
				url = compose_name_file_download(ftp_path,type_file)
				download(url,out_dir)
	print 'all files downloaded and saved at',out_dir
	



# csv = pd.read_csv("csvs/avium.csv")
# ftp_column = csv[rf_header]
# out_dir='out_genomes'
# for ftp_path in ftp_column:
# 	url = compose_name_file_download(ftp_path,"genbank")
# 	download(url,out_dir)


if __name__ == "__main__":
    #main(sys.argv[1:])
    main('genbank','out_genomes')
else:
    None

# #teste
# fh = open("csvs/favium.csv", "r")
# lines = fh.readlines()
# fh.close()
# #some pythonic magic
# header=lines[0]
# lines=lines[1:]
# fpt_index = search_ftp_column(header,rf_header)
# print rf_header,'column founded on position',fpt_index
# for line in lines:
# 	columns = line_header.split(",")
# 	ftp_path = columns[fpt_index]
# 	prin ftp_path

#ftp='ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/008/865/GCF_000008865.1_ASM886v1'
#ftype='genbank'

#print compose_name_file_download(ftp,ftype)

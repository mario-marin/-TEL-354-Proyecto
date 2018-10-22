import sys

open_path = sys.argv[1]
output_path = sys.argv[2]


file = open(open_path,'r');
output_file = open(output_path,'w');

init_flag = False

#----------------Static lookup tables-----------

indexes = {
	"StartTime": 0 ,
	"Dur": 1 ,
	"Proto": 2 ,
	"SrcAddr": 3 ,
	"Sport": 4 ,
	"Dir": 5 ,
	"DstAddr": 6 ,
	"Dport": 7 ,
	"State": 8 ,
	"sTos": 9 ,
	"dTos": 10 ,
	"TotPkts": 11 ,
	"TotBytes": 12 ,
	"SrcBytes": 13 ,
	"Label": 14 
}

direction = {
	"   ->": 1,
	"   ?>": 2,
	"  <?>": 3,
	"  <->": 4,
	"  <-": 5,
	"  who": 6,
	"  <?": 7
}

#----------------Search and edit----------------
for line in file: 
	#------------Pass header--------------------
	if init_flag == False:
		output_file.write(line)
		init_flag = True
		continue
	#------------Array creation-----------------
	line = line.rstrip() #trim de fat (\n)
	array = line.split(',')
	#------------control var--------------------

	#------------edit---------------------------
	array[indexes["Dir"]] = direction[array[indexes["Dir"]]]
	#------------output to file-----------------
	for x in range(0,len(array)):#convert everythong to string
		array[x] = str(array[x])
	line_to_write = ','.join(array) + "\n"
	output_file.write(line_to_write)



file.close()
output_file.close()
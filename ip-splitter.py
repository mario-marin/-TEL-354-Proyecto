import sys
from lookup_tables import *
import numpy as np

open_path = sys.argv[1]
output_path = "ip-botnet"


file = open(open_path,'r')
output_file = open(output_path,'w')

init_flag = False

#----------------Search and edit----------------
for line in file: 

	#------------Array creation-----------------
	line = line.rstrip() #trim de fat (\n)
	array = line.split(',')
	if init_flag == True:
			label = array[indexes["Label"]]
			label = label.split('-')
			label = label + label[0].split('=')
			botnet_flag = 0
			for x in range(0,len(label)):
				label[x] = label[x].lower()
				if(label[x] == "botnet"):
					botnet_flag = 1
					break
			if  botnet_flag == 0:
				continue
			array[indexes["Label"]] = 1
	else:
		init_flag = True
	trimed_array = array
	del trimed_array[indexes["dTos"]]
	del trimed_array[indexes["sTos"]]
	del trimed_array[indexes["State"]]
	
	for x in range(0,len(trimed_array)):#convert everythong to string
			trimed_array[x] = str(trimed_array[x])

	trimed_line = ','.join(trimed_array) + "\n"
	output_file.write(trimed_line)


file.close()
output_file.close()
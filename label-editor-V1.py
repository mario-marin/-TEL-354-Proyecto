import sys
from sklearn import datasets
import pandas as pd
from lookup_tables import *

open_path = sys.argv[1]
output_path = sys.argv[2]


file = open(open_path,'r');
output_file = open(output_path,'w');

output_file_bot = open("./output_test/1/data.txt",'w');
output_file_background = open("./output_test/0/data.txt",'w');

init_flag = False

max_ip = 255255255255


#----------------Search and edit----------------
for line in file: 

	#------------Array creation-----------------
	line = line.rstrip() #trim de fat (\n)
	array = line.split(',')
	#------------expand dictionary--------------
	if expand_state_flag:
		found_state = state.get(array[indexes["State"]])
		if found_state == None:
			state[array[indexes["State"]]] = state_count
			state_count+=1
	#------------control var--------------------

	if init_flag == True:
		#------------edit block---------------------
		#------------dir edit-----------------------
		array[indexes["Dir"]] = direction[array[indexes["Dir"]]]
		#------------proto edit---------------------
		array[indexes["Proto"]] = proto[array[indexes["Proto"]]]
		#------------state edit---------------------
		array[indexes["State"]] = state[array[indexes["State"]]]
		#------------label edit---------------------
		label = array[indexes["Label"]]
		label = label.split('-')
		label = label + label[0].split('=')
		botnet_flag = 0
		for x in range(0,len(label)):
			label[x] = label[x].lower()
			if(label[x] == "botnet"):
				botnet_flag = 1
		array[indexes["Label"]] = botnet_flag
		#------------ip edit------------------------
		ip_source= array[indexes["SrcAddr"]]
		ip_dest = array[indexes["DstAddr"]]
		ip_source = ip_source.split(".")
		ip_dest = ip_dest.split(".")
		ip_source = int(''.join(ip_source))/max_ip
		ip_dest = int(''.join(ip_dest))/max_ip
		array[indexes["SrcAddr"]] = ip_source
		array[indexes["DstAddr"]] = ip_dest
	#------------trim array---------------------
	trimed_array = array[1:]
	del trimed_array[-1]

	#------------output to file-----------------
	for x in range(0,len(array)):#convert everythong to string
		array[x] = str(array[x])
	for x in range(0,len(trimed_array)):#convert everythong to string
		trimed_array[x] = str(trimed_array[x])

	line_to_write = ','.join(array) + "\n"
	trimed_line = ','.join(trimed_array) + "\n"
	output_file.write(line_to_write)

	if init_flag == True:
		if botnet_flag == 1:
			output_file_bot.write(trimed_line)
		else:
			output_file_background.write(trimed_line)
	else:
		output_file_bot.write(trimed_line)
		output_file_background.write(trimed_line)
		init_flag = True

file.close()
output_file.close()
output_file_background.close()
output_file_bot.close()

if expand_state_flag:
	print(state)
	print(state_count)

'''
dataset = datasets.load_files("./output_test")
print(dataset)

pandas_dataset = pd.read_csv(output_path,header=1)
print(pandas_dataset)
'''
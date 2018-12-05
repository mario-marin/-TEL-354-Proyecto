import sys
from lookup_tables import *
import numpy as np

open_path = sys.argv[1]
output_path = sys.argv[2]


file = open(open_path,'r')
output_file = open(output_path,'w')

init_flag = False

max_ip = 255255255255
max_port = 65535
max_dur = 3660
max_dir = len(direction)
max_proto = len(proto)
max_state = len(state)
max_sTos = 192
max_totpkts =  16580642
max_totbytes = 4376238778
max_srcbytes = 2692621086


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
		#array[indexes["State"]] = state[array[indexes["State"]]]/max_state
		#------------label edit---------------------
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
			
			rand = np.random.uniform(high = 100.0)
			if rand > 5.0 :
				continue
			
		array[indexes["Label"]] = botnet_flag
		#------------ip edit------------------------ #se ignora ipv6 solo ocupa los primeros 2 octetos
		ip_source= array[indexes["SrcAddr"]]
		ip_dest = array[indexes["DstAddr"]]	
		ip_source = ip_source.split(".")
		ip_dest = ip_dest.split(".")
		try:
			ip_6_1 = 0
			ip_6_2 = 0
			ip_6_1 = ip_source[3]
			ip_6_2 = ip_dest[3]
			ip_source = (','.join(ip_source))
			ip_dest = (','.join(ip_dest))
		except Exception as e:
			print(ip_source)
			print(ip_dest)
			continue
		array[indexes["SrcAddr"]] = ip_source
		array[indexes["DstAddr"]] = ip_dest

		#------------port edit----------------------
		if array[indexes["Sport"]] == "" or array[indexes["Dport"]] == "":
			port_source = 0
			port_dest = 0
		else:
			port_source= array[indexes["Sport"]]
			port_dest = array[indexes["Dport"]]
			try:
				port_source = int(port_source)
				port_dest = int(port_dest)
			except Exception as e:
				port_source = int(port_source,16)
				port_dest = int(port_dest,16)
		array[indexes["Sport"]] = port_source
		array[indexes["Dport"]] = port_dest
		#------------dur edit-----------------------
		duration= array[indexes["Dur"]]
		duration = float(duration)
		array[indexes["Dur"]] = duration
		#------------sTos edit----------------------
		#debido a que se desconoce que este dato sera eliminado por el momento
		'''
		if array[indexes["sTos"]] == "":
			continue
		sTos= array[indexes["sTos"]]
		sTos = float(sTos)/max_sTos
		array[indexes["sTos"]] = sTos
		'''
		#------------dTos edit----------------------
		#debido a que se desconoce que este dato sera eliminado por el momento
		#------------Start time edit----------------
		#se considera que este valor no es relevante por ende sera eliminado por el momento
		#------------TotPkts edit-------------------
		TotPkts= array[indexes["TotPkts"]]
		TotPkts = float(TotPkts)/65535
		array[indexes["TotPkts"]] = TotPkts
		#------------TotBytes edit-------------------
		TotBytes= array[indexes["TotBytes"]]
		TotBytes = float(TotBytes)/65535
		array[indexes["TotBytes"]] = TotBytes
		#------------SrcBytes edit-------------------
		SrcBytes= array[indexes["SrcBytes"]]
		SrcBytes = float(SrcBytes)/65535
		array[indexes["SrcBytes"]] = SrcBytes

	#------------trim array---------------------
	trimed_array = array

	del trimed_array[indexes["dTos"]]
	del trimed_array[indexes["sTos"]]
	del trimed_array[indexes["State"]]
	del trimed_array[indexes["StartTime"]]
	

	#------------output to file-----------------
	#custom header
	if init_flag == False:
		output_file.write('Dur,Proto,SrcAddr_1,SrcAddr_2,SrcAddr_3,SrcAddr_4,Sport,Dir,DstAddr_1,DstAddr_2,DstAddr_3,DstAddr_4,Dport,TotPkts,TotBytes,SrcBytes,Label\n')
		init_flag = True
		continue

	for x in range(0,len(trimed_array)):#convert everythong to string
		trimed_array[x] = str(trimed_array[x])

	trimed_line = ','.join(trimed_array) + "\n"
	output_file.write(trimed_line)
	


file.close()
output_file.close()

if expand_state_flag:
	print(state)
	print(state_count)





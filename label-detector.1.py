import sys

path = sys.argv[1]

selected_label = sys.argv[2]
selected_label = selected_label.lower()

#--------------utility flags---------
create_dict = False
find_max = False

#------------------------------------
file = open(path,'r')

found_labels = []

total = 0

init_flag = False
max_value = 0
for line in file: 
	line = line.rstrip() #trim de fat (\n)
	#------------Find label---------------------
	if init_flag == False:
		array = line.split(',')
		if selected_label == "header":  #0.StartTime,1.Dur,2.Proto,3.SrcAddr,4.Sport,5.Dir,6.DstAddr,7.Dport,8.State,9.sTos,10.dTos,11.TotPkts,12.TotBytes,13.SrcBytes,14.Label
			print("File header: "+ str(array))
			exit()
		index = 0
		for element in array:
			element = element.lower()
			if selected_label == element:
				init_flag = True
				break
			index += 1
		if init_flag == False:
			print(selected_label + " not found in file header")
			exit()
		continue
	#------------label triming block------------
	array = line.split(',')
	label = array[index]
	#------------max finder---------------------
	if find_max:
		if label == "":
			continue
		if max_value < float(label): 
			max_value = float(label)
	#------------control var--------------------
	counter = 0
	flag = False
	#------------search loop--------------------
	if not find_max:
		for vector in found_labels:
			if vector[0] == label:
				vector[1] = vector[1] + 1
				total+=1
				flag = True
				break
			counter+=1

		if flag==False:
			found_labels.append([label,1])
			print(found_labels)
			total+=1
	#------------print reults--------------------
for x in found_labels:
	print(x)

if find_max:
	print("Max value: "+ str(max_value))
else:
	print("Total entries: " + str(total))
	print("Number of diferent labels: " + str(len(found_labels)))
if create_dict:
	counter = 0
	for x in found_labels:
		print("    "+'"'+str(x[0])+'"'+":"+" "+str(counter)+" ,")
		counter+=1


file.close()
import sys

path = sys.argv[1]

selected_label = sys.argv[2]
selected_label = selected_label.lower()

file = open(path,'r');

found_labels = []

total = 0

init_flag = False

for line in file: 
	line = line.rstrip() #trim de fat (\n)
	#------------Find label---------------------
	if init_flag == False:
		array = line.split(',')
		if selected_label == "header":  #StartTime,Dur,Proto,SrcAddr,Sport,Dir,DstAddr,Dport,State,sTos,dTos,TotPkts,TotBytes,SrcBytes,Label
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
	#------------control var--------------------
	counter = 0
	flag = False;
	#------------search loop--------------------
	for vector in found_labels:
		if vector[0] == label:
			vector[1] = vector[1] + 1
			total+=1
			flag = True
			break
		counter+=1

	if flag==False:
		found_labels.append([label,1])
		total+=1
	#------------print reults--------------------
for x in found_labels:
	print(x)
print("Total entries: " + str(total))
print("Number of diferent labels: " + str(len(found_labels)))

file.close()
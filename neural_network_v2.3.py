import sys
from sklearn.neural_network import MLPClassifier
import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np


testing_dataset_path = sys.argv[2]
training_dataset_path = sys.argv[1]

pd.set_option('precision',20)#indica cuandots decimales tiene el flotante
feature_cols = ["Dur","Proto","SrcAddr","Sport","Dir","DstAddr","Dport","TotPkts","TotBytes","SrcBytes"]
#feature_cols = ["Dur","Proto","SrcAddr_1","SrcAddr_2","SrcAddr_3","SrcAddr_4","Sport","Dir","DstAddr_1","DstAddr_2","DstAddr_3","DstAddr_4","Dport","TotPkts","TotBytes","SrcBytes"]

#USAGE: simplemente po todos los dataset con que quieres entrenar y el ultimo dataset sera el de prueba

#-------------training the model---------------

training_files = [f for f in listdir(training_dataset_path) if isfile(join(training_dataset_path, f))]

for x in range(0,len(training_files)):
	training_files[x] = training_dataset_path + training_files[x]

print(training_files)

testing_files = [f for f in listdir(testing_dataset_path) if isfile(join(testing_dataset_path, f))]

for x in range(0,len(testing_files)):
	testing_files[x] = testing_dataset_path + testing_files[x]

print(testing_files)


for path in training_files:
	print("Training with dataset : "+path)
	training_dataset = pd.read_csv(path,float_precision="high",dtype=float)
	training_dataset.fillna(0)
	X = training_dataset.loc[:,feature_cols]
	Y = training_dataset.Label


	activation_type = ['identity','logistic','tanh','relu']

	#vamos a probar con otras activaciones
	mlp = MLPClassifier(solver='sgd',learning_rate='adaptive',verbose=True,activation=activation_type[2])

	mlp.fit(X,Y)


print("Training done")


#------------testing the model-----------------

for path in testing_files:
	testing_dataset = pd.read_csv(path,float_precision="high",dtype=float)
	testing_dataset.fillna(0)
	X_testing = testing_dataset.loc[:,feature_cols]
	Y_testing = testing_dataset.Label

	predicted = mlp.predict(X_testing)

	true_0 = 0
	false_0 = 0
	true_1 = 0
	false_1 = 0


	for i in range(0,len(predicted)):

		if Y_testing[i] == 0.0:
			if predicted[i] == 0.0:
				true_0 += 1
			elif predicted[i] == 1.0:
				false_1 += 1

		elif Y_testing[i] == 1.0:
			if predicted[i] == 1.0:
				true_1 += 1
			elif predicted[i] == 0.0:
				false_0 += 1
	print("---------------------------------------------------")
	print("test with dataset: " + str(path))
	print("correct 0 : "+str(true_0))
	print("correct 1 : "+str(true_1))
	print("incorect 0 : "+str(false_0))
	print("incorect 1 : "+str(false_1))
	print("Final points given by mlp.score : "+str(mlp.score(X_testing,Y_testing)))

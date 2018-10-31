import sys
from sklearn.neural_network import MLPClassifier
import pandas as pd

del sys.argv[0]
testing_dataset_path = sys.argv[-1]
del sys.argv[-1]
training_dataset_path = sys.argv

pd.set_option('precision',20)#indica cuandots decimales tiene el flotante

#USAGE: simplemente po todos los dataset con que quieres entrenar y el ultimo dataset sera el de prueba

#-------------training the model---------------

for path in training_dataset_path:
	print("Training with dataset : "+path)
	training_dataset = pd.read_csv(path,float_precision="high",dtype=float)
	training_dataset.dropna(inplace=True) #drops rows with null values

	feature_cols = ["Dur","Proto","SrcAddr","Sport","Dir","DstAddr","Dport","State","TotPkts","TotBytes","SrcBytes"]
	X = training_dataset.loc[:,feature_cols]
	Y = training_dataset.Label


	mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 5,2))

	mlp.fit(X,Y)

print("Training done")

#------------testing the model-----------------

testing_dataset = pd.read_csv(testing_dataset_path,float_precision="high",dtype=float)
testing_dataset.dropna(inplace=True) #drops rows with null values

feature_cols = ["Dur","Proto","SrcAddr","Sport","Dir","DstAddr","Dport","State","TotPkts","TotBytes","SrcBytes"]
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


print("correct 0 : "+str(true_0))
print("correct 1 : "+str(true_1))
print("incorect 0 : "+str(false_0))
print("incorect 1 : "+str(false_1))

print("Final points given by mlp.score : "+str(mlp.score(X_testing,Y_testing)))
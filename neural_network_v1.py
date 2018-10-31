import sys
from sklearn.neural_network import MLPClassifier
import pandas as pd


training_dataset_path = sys.argv[1]
testing_dataset_path = sys.argv[2]

pd.set_option('precision',20)#indica cuandots decimales tiene el flotante

training_dataset = pd.read_csv(training_dataset_path,float_precision="high",dtype=float)
training_dataset.dropna(inplace=True) #drops rows with null values

feature_cols = ["Dur","Proto","SrcAddr","Sport","Dir","DstAddr","Dport","State","TotPkts","TotBytes","SrcBytes"]
X = training_dataset.loc[:,feature_cols]
Y = training_dataset.Label

mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 5,2))

mlp.fit(X,Y)

#training

testing_dataset = pd.read_csv(testing_dataset_path,float_precision="high",dtype=float)
testing_dataset.dropna(inplace=True) #drops rows with null values

feature_cols = ["Dur","Proto","SrcAddr","Sport","Dir","DstAddr","Dport","State","TotPkts","TotBytes","SrcBytes"]
X_testing = testing_dataset.loc[:,feature_cols]
Y_testing = testing_dataset.Label


print(mlp.predict(X_testing))
print(mlp.score(X_testing,Y_testing))
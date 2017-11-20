#NeuralNet with 9 input nodes, one hidden layer, and one output node
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

data = pd.read_csv('aima-data/restaurant.csv', names=["Alt", "Bar", "Fri/Sat", "Pat", "Price", "Rain", "Res", "Type", "Wait", "Answer"])

X = data.drop('Answer', axis=1)

y = data['Answer']

scaler = StandardScaler()

scaler.fit(X)

StandardScaler(copy=True, with_mean=True, with_std=True)

X_scal = scaler.transform(X)

mlp = MLPClassifier(hidden_layer_sizes=(3),max_iter=100000)

mlp.fit(X_scal, y)

print(mlp.coefs_)
print(mlp.intercepts_)
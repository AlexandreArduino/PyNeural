from PyNeural import PyNeural

network = PyNeural("datasets/covid_france.csv")
network.Train()
print(network.PredictValue())
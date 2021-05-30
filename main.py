from PyNeural import PyNeural

network = PyNeural("datasets/covid_france.csv")
datas = network.inputs
del network
for i in range(10):
    network = PyNeural("datasets/covid_france.csv")
    network.Train()
    datas.append(network.PredictValue())
    print(str(datas))
    del network
    file = open("datasets/covid_france.csv", "w")
    for j in range(0, len(datas)):
        file.write(str(datas[i]) + "\n")
    file.close()
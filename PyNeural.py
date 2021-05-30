from _csv_ import CSV
from random import randint
from time import sleep
class PyNeural(object):
    def __init__(self, csv_file):
        self.csv = CSV(csv_file)
        if not self.csv.ReadyToRead(): exit()
        else: self.datas = self.csv.ReadData()
        print(self.datas)
        '''
        The last data is the output for the training
        '''
        self.output = self.datas[len(self.datas)-1]
        del self.datas[len(self.datas)-1]
        self.inputs = self.datas
        del self.datas
        self.hiddens = [0.00, 0.00, 0.00, 0.00, 0.00]
        self.w1 = []
        self.w2 = []
        _cache = self.GetDeltaInInputs()
        self.da = -_cache
        self.db = _cache
        self.k = 5
        self.round = 2
        self.delay_time = .05
        del _cache
        self.SetWeights()
        self.Recap()
    def GetDeltaInInputs(self):
        self.delta = 0.00
        c = 0
        for i in range(2, len(self.inputs)):
            self.delta += abs(self.inputs[0] - self.inputs[i - 1])
            c += 1
        self.delta /= c
        del c
        return int(self.delta)
    def w(self): return (randint(self.da, self.db) + randint(0, 100)/100)*self.k
    def SetWeights(self):
        try: self.w1.clear()
        except: pass
        try: self.w2.clear()
        except: pass
        for i in range(0, len(self.inputs)*len(self.hiddens)): self.w1.append(self.w())
        for i in range(0, len(self.hiddens)): self.w2.append(self.w())
    def Recap(self):
        print("Recapping the training : ")
        print("\t- inputs => " + str(self.inputs))
        print("\t- output => " + str(self.output))
        print("\t- hidden neurals number => " + str(len(self.hiddens)))
    def Train(self):
        print("Training network ...")
        self.current_output = self.c()
        while self.current_output != self.output:
            self.SetWeights()
            self.current_output = self.c()
            sleep(self.delay_time)
    def c(self):
        for hidden_neural in range(len(self.hiddens)):
            cache = 0.00
            for input_neural in range(len(self.inputs)):
                cache += self.inputs[input_neural]*self.w1[input_neural+hidden_neural*len(self.inputs)]
                cache /= len(self.inputs)
                self.hiddens[hidden_neural] = cache
                del input_neural
            del hidden_neural
            cache = 0.00
            for hidden_neural in range(len(self.hiddens)):
                cache += self.hiddens[hidden_neural]*self.w2[hidden_neural]
        cache /= len(self.hiddens)
        del hidden_neural
        return int(cache)
    def PredictValue(self):
        self.inputs.append(self.output)
        return self.c()
class CSV(object):
    def __init__(self, path):
        print("[WARNING] CSV module can't read more than one column in a CSV file!")
        self.CorrectFile = False
        self.datas = []
        if not self.IsCorrectFile(path):
            print("[CSV] Incorrect file/path!")
        else: self.path = path
    def IsCorrectFile(self, path):
        try:
            file = open(path, "r")
            file.close()
            self.CorrectFile = True
            return True
        except: return False
    def ReadyToRead(self): return self.CorrectFile
    def ReadData(self):
        if not self.CorrectFile:
            print("You can't read datas from no file!")
        else:
            file = open(self.path, "r")
            l = file.readlines()
            file.close()
            for i in range(0, len(l)):
                l[i] = l[i].replace("\n", "")
                try:
                    l[i] = int(l[i])
                except: del l[i]
            self.datas = l
        return self.datas #Keeping self.datas in memory for others functions if it is needing
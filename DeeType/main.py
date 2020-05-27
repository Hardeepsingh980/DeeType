class DeeType:

    def __init__(self, l):
        if type(l) != list:
            raise 'This Package Only Support List As Parameter'
        self.l = l

    def findStr(self):
        res = []
        for i in self.l:
            if type(i) == str:
                res.append(i)

        return res

    def findInt(self):
        res = []
        for i in self.l:
            if type(i) == int:
                res.append(i)

        return res

    def findList(self):
        res = []
        for i in self.l:
            if type(i) == list:
                res.append(i)

        return res

    def findDict(self):
        res = []
        for i in self.l:
            if type(i) == dict:
                res.append(i)

        return res

    def findBool(self):
        res = []
        for i in self.l:
            if type(i) == bool:
                res.append(i)

        return res

    def showTypeDict(self):
        return {
            'strings': self.findStr(),
            'integers': self.findInt(),
            'booleans': self.findBool(),
            'lists': self.findList(),
            'dicts': self.findDict()
        }



if __name__ == "__main__":
    d = DeeType(1)
    print(d.showTypeDict())
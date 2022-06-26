class Students():
    def __init__(self):
        self.dictionary = {}

    def add(self, name:str, id:str):
        self.dictionary[name] = id

    def list(self):
        temp = []
        for x, y in self.dictionary.items():
            temp.append((x, y))
        return temp

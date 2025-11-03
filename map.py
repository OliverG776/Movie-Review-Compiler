class Map:
    def __init__(self):
        self.mapContainer = [None] * 10
        self.load_factor = 0.0
        self.buckets = 0

    def __setitem__(self, title, values):
        genres, rating = values
        self.insert(title, genres, rating)

    def __hash__(self, key):
        pow = 0
        sum = 0
        for i in str(key):
            sum += ord(i)*27**pow
            pow+=1
        return sum%len(self.mapContainer)

    def probe(self, index):
        pow = 1;
        newIndex = index
        while not(self.mapContainer[newIndex] is None):
            newIndex = (index + pow**2) % len(self.mapContainer)
            pow += 1
        return newIndex;

    def insert(self, title, genres, rating):
        keyHash = self.__hash__(title)
        if self.mapContainer[keyHash] is None:
            self.mapContainer[keyHash] = (title,genres,rating)
            self.buckets += 1
        else:
            keyHash = self.probe(keyHash)
            self.mapContainer[keyHash] = (title,genres,rating)
            self.buckets+=1

        self.load_factor = self.buckets / len(self.mapContainer)
        if self.load_factor > 0.7:
            self.resize()

    def resize(self):
        oldMap = self.mapContainer
        newSize = len(self.mapContainer)*2
        self.mapContainer = [None]*newSize
        self.buckets = 0
        for i in oldMap:
            if i:
                self.insert(i[0],i[1], i[2])
        self.load_factor = self.buckets/len(self.mapContainer)

    def __contains__(self, item):
        return item in self.dataType1

    def getKeys(self):
        return self.dataType1.keys()

    def getValues(self):
        return self.dataType1.values()

    def getItems(self):
        return self.dataType1.items()

    def search(self, key):

        return True

    def __getitem__(self, key):
        self.search(key)
        return key

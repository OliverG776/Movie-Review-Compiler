class Map:
    def __init__(self, dataType1, dataType2):
        self.dataType1 = dataType1
        self.dataType2 = dataType2
        self.mapContainer = [None] * 10
        self.load_factor = 0.0
        self.buckets = 0

    def __getitem__(self, key):
        return self.dataType1[key]

    def __setitem__(self, key, value):

        self.dataType1[key] = value


    def __delitem__(self, key):
        del self.dataType1[key]

    def __eq__(self, other):
        return self.dataType1 == other.dataType1 and self.dataType2 == other.dataType2

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
        while not(self.mapContainer[newIndex] is None) and (self.mapContainer[newIndex][0] != "<deletedBucket>"):
            newIndex = (index + pow**2) % len(self.mapContainer)
            pow += 1
        return newIndex;

    def insert(self, key, value):
        keyHash = self.__hash__(key)
        if self.mapContainer[keyHash] is None:
            self.mapContainer[keyHash] = (key,value)
            self.buckets += 1
        elif self.mapContainer[keyHash] and (self.mapContainer[keyHash][0] == "<deletedBucket>"):
            self.mapContainer[keyHash] = (key,value)
            self.buckets += 1
        else:
            keyHash = self.probe(keyHash)
            self.mapContainer[keyHash] = (key,value)
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
            if i and (i[0] != "<deletedBucket>"):
                self.insert(i[0],i[1])
        self.load_factor = self.buckets/len(self.mapContainer)

    def __contains__(self, item):
        return item in self.dataType1

    def getKeys(self):
        return self.dataType1.keys()

    def getValues(self):
        return self.dataType1.values()

    def getItems(self):
        return self.dataType1.items()

    def clear(self):
        self.dataType1 = None

    def search(self, key):
        return True

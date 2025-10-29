class Map:
    def __init__(self, dataType1, dataType2):
        self.dataType1 = dataType1
        self.dataType2 = dataType2
        self.mapContainer = [0] * 10

    def __getitem__(self, item):
        return self.dataType1[item]

    def __setitem__(self, key, value):
        self.dataType1[key] = value

    def __delitem__(self, key):
        del self.dataType1[key]

    def __eq__(self, other):
        return self.dataType1 == other.dataType1 and self.dataType2 == other.dataType2

    def __hash__(self):
        return hash(self.dataType1)

    def resize(self, width, height):
        return 0

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
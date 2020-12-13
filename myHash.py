# Mark Murphy, 001223523


# Very basic direct hashtable
class Hash(object):

    def __init__(self, hashSize=1000000):
        self.hashTable = [None] * hashSize
        self.hashSize = hashSize
        self.size = 0

    def insert(self, parcel):
        self.hashTable[parcel.idNumber % self.hashSize] = parcel
        self.size += 1

    def search(self, idNumber):
        return self.hashTable[idNumber % self.hashSize]

    def delete(self, idNumber):
        if self.search(idNumber):
            self.hashTable[idNumber % self.hashSize] = None
            self.size -= 1
        else:
            return None

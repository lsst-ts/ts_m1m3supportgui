class BitHelper:
    def get(word, bit):
        return word & (1 << bit) != 0

    def getBit(word, bit):
        if (word & (1 << bit)) != 0:
            return 1
        return 0

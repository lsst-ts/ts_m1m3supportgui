
class BitHelper:
    def get(word, bit):
        return word & (1 << bit) != 0
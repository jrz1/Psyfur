import operator as o
from string import ascii_lowercase as alphabet_lower
from string import ascii_uppercase as alphabet_upper

class CiceroCipher(object):

    def __init__(self, word, n=5):
        self.original_word = word
        self.shift_word = word
        self.n = n

    def __shift(self, x, encrypt):
        op = o.add if encrypt else o.sub
        alphabet = alphabet_lower if x in alphabet_lower else alphabet_upper
        return alphabet[(op(alphabet.index(x), self.n)) % 26]

    def __process(self, encrypt=True):
        s = []
        PUNCT = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        for i,l in enumerate(self.shift_word):
            if encrypt:
                self.n += i
            else:
                self.n -= i
            s.append(l if l in PUNCT else self.__shift(l, encrypt))
        self.shift_word = ''.join(s)
        return self.shift_word

    def encrypt(self):
        return self.__process(encrypt=True)

    def decrypt(self):
        return self.__process(encrypt=False)

def main():
    c = CiceroCipher("My name is John, and I am evil!", 5)
    c.encrypt()

    print "Shifted Word:  {sw}".format(sw=c.shift_word)
    print "Original Word: {ow}".format(ow=c.original_word)

if __name__ == '__main__':
    main()

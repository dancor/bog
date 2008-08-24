class Trie:
    def __init__(self):
        self.root = {}
    def add(self, key):
        node = self.root
        for ch in list(key):
            try:
                node = node[ch]
            except KeyError:
                node[ch] = {}
                node = node[ch]
        node['.'] = True
    def isWd(self, key):
        '''return None if no word has this prefix, True if this is a word, 
        False otherwise'''
        node = self.root
        for ch in list(key):
            try:
                node = node[ch]
            except KeyError:
                return None
        try:
            return node['.']
        except KeyError:
            return False

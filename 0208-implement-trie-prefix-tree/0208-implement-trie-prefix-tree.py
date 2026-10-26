class Trie:

    def __init__(self):
        self.child={}
        self.isend=False

    def insert(self, word: str) -> None:
        node=self
        for ch in word:
            if ch not in node.child:
                node.child[ch]=Trie()
            node=node.child[ch]
        node.isend=True

    def search(self, word: str) -> bool:
        node=self
        for ch in  word :
            if ch  not in node.child:
                return False
            else:
                node=node.child[ch]
        if node.isend:
            return True
        else:
            return False
        
    def startsWith(self, prefix: str) -> bool:
        node=self
        for ch in  prefix :
            if ch  not in node.child:
                return False
            else:
                node=node.child[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
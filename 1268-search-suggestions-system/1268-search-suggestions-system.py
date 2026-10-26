class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        class Trie:
            def __init__(self):
                self.child={}
                self.isend=False
            def insert(self,products):
                for word in products:
                    node=self
                    for ch in word:
                        if ch not in node.child:
                            node.child[ch]=Trie()
                        node=node.child[ch]
                    node.isend=True

            def search(self,word):
                ans=[]
                node=self
                for ch in word:
                    if ch not in node.child:
                        return []
                    else:
                        node=node.child[ch]

                def dfs(node,word):
                    if (len(ans)==3):
                        return 
                    if node.isend:
                        ans.append(word)
                        
                    for x in sorted(node.child):
                        temp=node
                        node=node.child[x]
                        dfs(node,word+x)
                        node=temp
                dfs(node,word)
                return ans

        answer=[]
        product=Trie()
        product.insert(products)

        prefix=""
        for i in range(0,len(searchWord)):
            prefix+=searchWord[i]
            answer.append(product.search(prefix))
        return answer



        
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        best_guess=words[0]
        while(words):
            mini=master.guess(best_guess)
            if (mini==6):
                return 
            guessed=best_guess
            words.remove(guessed)
            temp=words.copy()           
            for i in temp:
                    ans=sum(x == y for x, y in zip(i, guessed))
                    if (ans==mini):
                        continue
                    else:
                        words.remove(i)
            

            best_score=float("inf")
            for guess in words:
                groups={}      
                for i in words:   
                    matches=sum(x == y for x, y in zip(i,guess)) 
                    if (matches not in groups):
                        groups[matches]=0
                    groups[matches]+=1
                largest=max(groups.values())
                if (largest<best_score):
                    best_score=largest
                    best_guess=guess

                    
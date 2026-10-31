class RandomizedSet:

    def __init__(self):
        self.random={}
        self.arr=[]
        self.count=0
    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.arr.append(val)
            self.random[val]=self.count
            self.count+=1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.random:
            idx=self.random[val]
            self.arr[idx]=self.arr[-1]
            self.random[self.arr[-1]]=idx
            self.arr.pop()
            self.random.pop(val)
            self.count-=1
            return True
        else:
            return False

    def getRandom(self) -> int:
            return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
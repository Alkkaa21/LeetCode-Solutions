class FreqStack(object):

    def __init__(self):
        self.cnt={}
        self.maxCnt=0
        self.stacks={}
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        valcnt = 1+ self.cnt.get(val,0)
        self.cnt[val]=valcnt
        if valcnt not in self.stacks:
            self.stacks[valcnt] = []
        self.stacks[valcnt].append(val)
        self.maxCnt = max(self.maxCnt,valcnt)
        

    def pop(self):
        """
        :rtype: int
        """
        res=self.stacks[self.maxCnt].pop()
        self.cnt[res]-=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt-=1
        return res
         
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
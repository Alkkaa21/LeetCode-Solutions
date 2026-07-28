#Given two arrays, deadline[] and profit[], where deadline[i] is the last time unit by which the i-th job must be completed, and profit[i] is the profit earned from completing it.
#Each job takes 1 unit time, and only one job can be scheduled at a time. A job earns profit only if finished within its deadline. Find the number of jobs completed and maximum profit.
#Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
#Output: [2, 60]
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs=list(zip(profit,deadline))
        jobs.sort(reverse=True)
        max_deadline=max(deadline)
        slots=[False]*(max_deadline+1)
        count,tot_profit=0,0
        for p,d in jobs:
            for slot in range(d,0,-1):
                if not slots[slot]:
                    slots[slot]=True
                    count+=1
                    tot_profit+=p
                    break
        return[count,tot_profit]
        # code here
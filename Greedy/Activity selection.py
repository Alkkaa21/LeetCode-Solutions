#Given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. A single person can perform only one activity at a time, meaning no two activities can overlap. Your task is to determine the maximum number of activities that a person can complete in a day.

#Note: Start time and finish time cannot overlap, i.e., if a person finishes an activity at time x, then they cannot start another activity at time x.

#Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
#Output: 4
class Solution:
    def activitySelection(self, start, finish):
        #code here
        activities=list(zip(finish,start))
        activities.sort()
        if not activities:
            return 0
        last_fin=activities[0][0]
        count=1
        for finish,strt in activities[1:]:
            if strt>last_fin:
                count+=1
                last_fin=finish
        return count
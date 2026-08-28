class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)
        for first, last, seats in bookings:
            answer[first-1]+=seats
            answer[last]-=seats
        prefix=0
        for i in range(len(answer)):
            prefix+=answer[i]
            answer[i]=prefix
        return answer[:n]

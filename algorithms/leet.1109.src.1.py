class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n+1)
        for l, r, x in bookings:
            arr[l-1] += x
            arr[r] -= x
        for i in range(1, n):
            arr[i] += arr[i-1]
        return arr[:-1]

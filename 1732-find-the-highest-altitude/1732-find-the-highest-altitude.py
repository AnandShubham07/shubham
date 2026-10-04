class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n=len(gain)
        altitudes=[0]
        for i in range(0,n):
            altitudes.append(altitudes[i]+gain[i])
        return max(altitudes)

        
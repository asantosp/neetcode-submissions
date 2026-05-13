class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSoFar = 0
        consecutiveOnes = 0
        for i in nums:
            if i == 1:
                consecutiveOnes += 1
            else:
                if (consecutiveOnes > maxSoFar):
                    maxSoFar = consecutiveOnes
                consecutiveOnes = 0
        if (consecutiveOnes > maxSoFar):
            maxSoFar = consecutiveOnes
        return maxSoFar
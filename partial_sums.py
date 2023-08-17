    def maxSumSubarray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                maxSum = max(maxSum, sum)
        return maxSum


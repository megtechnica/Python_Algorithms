    def maxSumSubarray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                maxSum = max(maxSum, sum)
        return maxSum

    def maxSumOfThreeSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        for i1 in range(n):
            sum1 = 0
            for j1 in range(i1, n):
                sum1 += nums[j1]
                for i2 in range(j1 + 1, n):
                    sum2 = 0
                    for j2 in range(i2, n):
                        sum2 += nums[j2]
                        for i3 in range(j2 + 1, n):
                            sum3 = 0
                            for j3 in range(i3, n):
                                sum3 += nums[j3]
                                maxSum = max(maxSum, sum1 + sum2 + sum3)
        return maxSum



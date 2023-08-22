  def maxSumSubarray(self, nums):
      result = nums[0]
      maxSum = 0
      for val in nums:
          maxSum = val + max(maxSum, 0)
          result = max(result, maxSum)
      return result

  def maxSumOfThreeSubarrays(self, nums: List[int]) -> int:
      n = len(nums)
      maxSum = float('-inf')
      for i in range(1, n):
          sum1 = self.maxSumSubarray(nums[ : i])
          sum2 = 0
          for j in range(i, n - 1):
              sum2 += nums[j]
              sum3 = self.maxSumSubarray(nums[j + 1 : ])
              maxSum = max(maxSum, sum1 + sum2 + sum3)
      return maxSum
    

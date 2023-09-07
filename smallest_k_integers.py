class SmallestKIntegers:
    def partition(self, nums, left, right):
        randomIndex = left + random.randint(0, right - left)
        nums[randomIndex], nums[right] = nums[right], nums[randomIndex]
        value = nums[right]
        correctIndex = left
        for i in range(left, right + 1):
            if nums[i] <= value:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
                correctIndex += 1
        return correctIndex - 1
    
    def smallestKNums(self, nums, left, right, k):
        if left >= right:
            return
        pivot = self.partition(nums, left, right)
        if pivot - left + 1 >= k:
            self.smallestKNums(nums, left, pivot - 1, k)
        else:
            self.smallestKNums(nums, pivot + 1, right, k - (pivot - left + 1))

    def kSmallest(self, nums: List[int], k: int) -> List[int]:
        self.smallestKNums(nums, 0, len(nums) - 1, k)
        return nums[0:k]
        

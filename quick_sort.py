class QuickSort:
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

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = self.partition(nums, left, right)
        self.quickSort(nums, left, pivot - 1)
        self.quickSort(nums, pivot + 1, right)

    def sort(self, nums: List[int]):
        self.quickSort(nums, 0, len(nums) - 1)

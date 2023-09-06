class MergeSort:
    def mergeSubarrays(self, nums, left, middle, right):
        i = left
        j = middle + 1
        k = left
        while i <= middle and j <= right:
            if nums[i] < nums[j]:
                self.temp[k] = nums[i]
                i += 1
            else:
                self.temp[k] = nums[j]
                j += 1
            k += 1

        while i <= middle:
            self.temp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            self.temp[k] = nums[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            nums[i] = self.temp[i]


    def mergeSort(self, nums, left, right):
        if left == right:
            return
        middle = (left + right) // 2
        self.mergeSort(nums, left, middle)
        self.mergeSort(nums, middle + 1, right)
        self.mergeSubarrays(nums, left, middle, right)

    def sort(self, nums: List[int]):
        self.temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1)


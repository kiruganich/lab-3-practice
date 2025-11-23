class Solution(object):
    def sortColors(self, nums):
        arr = nums
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] >= arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
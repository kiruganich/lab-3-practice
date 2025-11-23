class Solution:
    def topKFrequent(self, nums, k):
        c = {}

        for n in nums:
            c[n] = 1 + c.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in c.items():
            freq[f].append(n)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
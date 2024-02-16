class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(n)

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(nlogn)

        # hmap = {}
        # op = []

        # for i in range(0, len(nums)):
        #     count = 0
        #     if nums[i] not in hmap.keys():
        #         hmap[nums[i]] = count + 1
        #     else:
        #         count = hmap[nums[i]]
        #         hmap[nums[i]] = count + 1

        # key = sorted(hmap, key=hmap.get, reverse=True)

        # for x in range(0, k):
        #     op.append(key[x])

        # return op

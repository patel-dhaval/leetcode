class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        total = count = 0
        for n in nums:
            total += n
            target = total - k
            if target in prefix_map:
                count += prefix_map.get(target)
            prefix_map[total] += 1
        
        return count
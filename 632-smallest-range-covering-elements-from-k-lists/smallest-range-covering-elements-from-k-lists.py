class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        min_heap = []
        current_max = float('-inf')
        for idx in range(k):
            if nums[idx][0] > current_max:
                current_max = nums[idx][0]
            min_heap.append((nums[idx][0],idx,0))
        
        heapq.heapify(min_heap)

        best_range = [float('-inf'), float('inf')]
        
        while min_heap:
            # 1. Pop the minimum element and unpack its metadata
            current_min, list_idx, item_idx = heapq.heappop(min_heap)
            
            # 2. (Insert logic here to check if [current_min, current_max] is our new best range)

            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]

            # 3. Find the NEXT element in this specific list
            next_item_idx = item_idx + 1
            
            # 4. Check if this specific list has run out of numbers
            if next_item_idx == len(nums[list_idx]):
                break # We hit the end of one list. We can no longer cover all K lists! Stop the system.
                
            # 5. Grab the new number, update our max ceiling, and push the new metadata into the heap
            next_value = nums[list_idx][next_item_idx]
            
            current_max = max(current_max, next_value)
            heapq.heappush(min_heap, (next_value, list_idx, next_item_idx))        

        return best_range
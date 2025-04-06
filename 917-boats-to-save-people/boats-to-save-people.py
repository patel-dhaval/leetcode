"""
ip : 1223
l = 1
r = 3, 2
limit = 3
count = 1, 2, 3

"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people)-1

        while l <= r:
            if people[l] + people[r] <= limit:
                l+=1
                r-=1
                count +=1
            elif people[r] <= limit:
                r-=1
                count+=1
            elif people[l] <= limit:
                l+=1
                count +=1
            elif l == r:
                count +=1
                l+=1
                r-=1
        
        return count
                
                
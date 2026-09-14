class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        print(d)
        has_dup = 0
        for i,j in d.items():
            if j > 1:
                has_dup = 1
        if has_dup == 1: return True
        return False
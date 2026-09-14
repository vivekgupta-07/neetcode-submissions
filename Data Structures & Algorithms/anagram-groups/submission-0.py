class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)
        result = sorted(d.values(),key=len)
        return result
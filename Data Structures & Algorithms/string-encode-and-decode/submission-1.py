class Solution:

    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            # 1. Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract length and the string segment
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 3. Move i to the next encoded chunk
            i = end

        return res
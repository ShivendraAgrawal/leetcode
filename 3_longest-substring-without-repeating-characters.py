class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        start = 0
        max_gap = 1

        for i in range(1, len(s)):
            end = i
            j = i - 1
            while (j >= start):
                print("i = ",i , ", j = ", j)
                if s[i] != s[j]:
                    j -= 1
                    gap = end - j
                    if gap > max_gap:
                        max_gap = gap
                else:
                    gap = end - start
                    if gap > max_gap:
                        max_gap = gap
                    start = j + 1
        return max_gap


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcab"))
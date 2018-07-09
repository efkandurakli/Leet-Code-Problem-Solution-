class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        first_index = 0
        last_index = 0
        i = 0
        set = {1}
        while i < len(s):
            if (s[i] not in set):
                set.add(s[i])
                last_index += 1
                i += 1
            else:
                max_len = max(max_len, last_index-first_index)
                set.clear()
                first_index += 1
                last_index = first_index
                i = first_index

        return max(max_len, last_index-first_index)




sol = Solution()

print(sol.lengthOfLongestSubstring("pwwek"))
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        digitList = []

        if (x < 0):
            return False

        while (x > 0):
            digitList.append(x % 10)
            x = (int)(x / 10)

        first = 0
        last = len(digitList)-1
        while (first < last):
            if (digitList[first] != digitList[last]):
                return False
            first += 1
            last -= 1

        return True






sol = Solution()

print(sol.isPalindrome(121))
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x < -2147483648 or x > 2147483647):
            return 0;


        reverse = 0;
        negative = False

        if (x < 0):
            negative = True
            x = -1*x

        while (x > 0):
            lastDigit = x % 10
            reverse = (reverse*10) + lastDigit
            x = (int) (x / 10)


        if (reverse < -2147483648 or reverse > 2147483647):
            return 0;


        if (negative):
            reverse = -1*reverse
        return reverse




sol = Solution()

print(sol.reverse(1534236469))

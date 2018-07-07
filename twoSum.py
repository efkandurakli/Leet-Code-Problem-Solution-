class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target and i != j):
                    retList.append(i)
                    retList.append(j)
                    return retList
        return retList




sol = Solution()

list = [2,7,11,15]

retList = sol.twoSum(list,9)

print(retList)



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        i = 0
        j = 0
        destArray = []
        while (i < len(nums1) and j < len(nums2)):
            if (nums1[i] < nums2[j]):
                destArray.append(nums1[i])
                i += 1
            else:
                destArray.append(nums2[j])
                j += 1

        if (i >= len(nums1)):
            while (j < len(nums2)):
                destArray.append(nums2[j])
                j += 1
        else:
            while (i < len(nums1)):
                destArray.append(nums1[i])
                i += 1

        return self.medianOfArray(destArray)



    def medianOfArray(self, array):
        if (len(array) % 2 == 1):
            return array[int(len(array)/2)]
        else:
            return (array[int(len(array)/2)] + array[int(len(array)/2) - 1])/2



sol = Solution()

nums1 = [1,2,8]
nums2 = [3,4,9]

print(sol.findMedianSortedArrays(nums1,nums2))
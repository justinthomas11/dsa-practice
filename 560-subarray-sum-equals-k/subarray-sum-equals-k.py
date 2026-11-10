class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count= 0
        sum= 0
        hashmap = {0:1}

        for num in nums:
            sum+=num

            if sum-k in hashmap:
                count += hashmap[sum-k]

            hashmap[sum] = hashmap.get(sum,0) + 1

        return count

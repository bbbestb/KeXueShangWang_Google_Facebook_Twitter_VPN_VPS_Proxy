# *_* coding=utf-8 *_*

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

链接：https://leetcode-cn.com/problems/two-sum

1. 暴力破解：时间复杂度 O(N^2)  空间复杂度 O(1)
2. 哈希表：时间复杂度 O(N)  空间复杂度 O(N)

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return ['not-found', 'not-found']
    
    def twoSum_1(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return ['not-found', 'not-found']


if __name__ == '__main__':
    num_list = [1, 7, 9, 4, 53, 42]
    sum = 62
    s = Solution()
    print(s.twoSum(num_list, sum))
    print(s.twoSum_1(num_list, sum))
    num_list = [3, 2, 4]
    sum = 6
    print(s.twoSum(num_list, sum))
    print(s.twoSum_1(num_list, sum))
    num_list = [3, 3]
    sum = 6
    print(s.twoSum(num_list, sum))
    print(s.twoSum_1(num_list, sum))

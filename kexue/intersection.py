# -*- coding:UTF-8 -*-
'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]


说明：
    * 输出结果中的每个元素一定是唯一的。
    * 我们可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        元组set 是基于Hash来实现的，故：
        1. set 中的元素必须唯一（不可重复）
        2. set 中的元素必须是Hashable的
        3. 向集合中添加元素、删除元素、检查元素是否存在，都是非常快速的。平均时间复杂度为O(1),最坏的时间复杂度是O(n)
        
        本算法 时间复杂度 O(n+m)  空间复杂度 O(n+m)
        """
        ret = []
        s1 = set(nums1)
        s2 = set(nums2)
        # 考虑到检查集合中元素O(1)的复杂度，所以只遍历较小的集合是时间复杂度更低的
        if len(s1) > len(s2):
            ret = [i for i in s2 if i in s1]
        else:
            ret = [i for i in s1 if i in s2]
        return ret


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    s = Solution()
    print(s.intersection(nums1, nums2))

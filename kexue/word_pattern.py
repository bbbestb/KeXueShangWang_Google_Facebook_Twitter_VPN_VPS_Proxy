# *_* coding=utf-8 *_*

'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

说明: 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

链接：https://leetcode-cn.com/problems/word-pattern

以第2中为例：时间复杂度O(n+m)，空间复杂度O(n+m)
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_list = s.strip().split()
        my_map = dict()
        if len(pattern) != len(s_list):
            return False
        for i, j in zip(pattern, s_list):
            if i in my_map:
                if my_map[i] != j:
                    return False
            else:
                if j in my_map.values():
                    return False
                else:
                    my_map[i] = j
        return True
    
    def wordPattern_1(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_list = s.strip().split()
        ch_map = dict()
        word_map = dict()
        if len(pattern) != len(s_list):
            return False
        for i, j in zip(pattern, s_list):
            if (i in ch_map and ch_map[i] != j) or (j in word_map and word_map[j] != i):
                return False
            else:
                ch_map[i] = j
                word_map[j] = i
        return True

    def wordPattern_2(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        res=s.split()
        return list(map(pattern.index, pattern))==list(map(res.index,res))


if __name__ == '__main__':
    s = Solution()
    p1 = 'abba'
    s1 = 'dog cat cat dog'
    print(s.wordPattern(p1, s1))
    print(s.wordPattern_1(p1, s1))
    print(s.wordPattern_2(p1, s1))
    p2 = 'abba'
    s2 = 'dog cat cat fish'
    print(s.wordPattern(p2, s2))
    print(s.wordPattern_1(p2, s2))
    print(s.wordPattern_2(p2, s2))
    p3 = 'abba'
    s3 = 'dog dog dog dog'
    print(s.wordPattern(p3, s3))
    print(s.wordPattern_1(p3, s3))
    print(s.wordPattern_2(p3, s3))

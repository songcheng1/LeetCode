# 两数之和（返回对应索引）

        # 答案1:
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                lens = len(nums)
                j=-1
                for i in range(1,lens):
                    temp = nums[:i]
                    if (target - nums[i]) in temp:
                        j = temp.index(target - nums[i])
                        break
                if j>=0:
                    return [j,i]

        # 答案2:
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                lens = len(nums)
                j=-1
                for i in range(1,lens):
                    temp = nums[:i]
                    if (target - nums[i]) in temp:
                        j = temp.index(target - nums[i])
                        break
                if j>=0:
                    return [j,i]
           
# **********************************************************************************************************
# 9. 回文数

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]

# **********************************************************************************************************
# 13. 罗马数字转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        temp_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):
            if temp_dict[s[i]]<temp_dict[s[i+1]]:
                result -= temp_dict[s[i]]
            else:
                result += temp_dict[s[i]]
        result += temp_dict[s[-1]]
        return result
# **********************************************************************************************************
# 14. 最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            b = sorted(strs, key=lambda x:len(x)) # 按字符串的长度进行排序
            s = ''
            s1 = b[0]
            for i, v in enumerate(s1): # 对第一个字符串进行枚举，遍历其每一个字符
                l = []
                for j in b[1:]:		   # 从第二个字符串开始遍历之后的所有字符串
                    l.append(v==j[i])  # 将字符比较的bool值添加到列表l中
                if all(l):			   # 如果列表l中的所有值都为True
                    s += v
                else:
                    break
            return s



# **********************************************************************************************************
# 20. 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

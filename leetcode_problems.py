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

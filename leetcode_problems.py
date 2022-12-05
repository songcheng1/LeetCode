# 1.两数之和（返回对应索引）
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
            ts = []
            for index1, v1 in enumerate(nums):
                for index2, v2 in enumerate(nums):
                    if v1 + v2 == target and index1 != index2:
                        ts.append(index1)
                        ts.append(index2)
                if ts:
                    break
            return ts

# **********************************************************************************************************
# 9. 回文数

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]

# **********************************************************************************************************
# 125. 验证回文串
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        new_strs = re.findall("[A-Za-z0-9]+", s)
        new_str = new_strs[0] if new_strs else s
        if new_str == new_str[::-1]:
            return True
        else:
            return False


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



# **********************************************************************************************************
# 21. 合并两个有序链表
        
        # 答案1:
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution:
            def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                if not l1 and not l2:
                    return None
                if not l1 and l2:
                    return l2
                if l1 and not l2:
                    return l1
                headForList = ListNode(0)
                myListNode = headForList
                while l1 and l2:
                    if l1.val <= l2.val:
                        myListNode.next = l1
                        l1 = l1.next
                    else:
                        myListNode.next = l2
                        l2 = l2.next
                    myListNode = myListNode.next
                if l1:
                    myListNode.next = l1
                else:
                    myListNode.next = l2
                return headForList.next
        
        # 答案2:
        class Solution:
            def mergeTwoLists(self, list1, list2):
                new_lists = list1 + list2
                new_lists.sort()
                return new_lists
        
# **********************************************************************************************************
# 26. 删除有序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast] != nums[fast -1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# **********************************************************************************************************
# 70. 爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = res[1] =1 
        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[-1]  

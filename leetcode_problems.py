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
# 27. 移除元素
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        index = 0
        m = len(nums)
        for i in range(m):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
    
    
# **********************************************************************************************************
# 35. 搜索插入位置   
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for index_, i in enumerate(nums):
                if target==i:
                    return index_
        else:
            nums.append(target)
            nums.sort()
            for j_index, j in enumerate(nums):
                if target==j:
                    return j_index
                
                
# **********************************************************************************************************
# 58. 最后一个单词的长度                 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(' ')
        for i in range(len(res)):
            if res[len(res)-i-1] != '':
                return len(res[len(res)-i-1])
        return 0
    
    

# **********************************************************************************************************
# 66. 加一   
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for site in range(len(digits)-1, -1, -1):
            if digits[site] != 9:
                digits[site] += 1
                return digits
            else:
                digits[site] = 0
        digits.insert(0,1)
        return digits

    
# **********************************************************************************************************
# 67. 二进制求和     
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length1 = len(a)
        length2 = len(b)
        if length1 < 1 or length1 > 10 ** 4:
            return 
        if length2 < 1 or length2 > 10 ** 4:
            return
        result = ""
        carry_out = 0
        index1 = length1 - 1
        index2 = length2 - 1
        while index1 >= 0 or index2 >= 0 or carry_out == 1:
            if index1 >= 0:
                auxiliary1 = int(a[index1])
            else:
                auxiliary1 = 0
            if index2 >= 0:
                auxiliary2 = int(b[index2])
            else:
                auxiliary2 = 0
            carry_out, auxiliary3 = divmod(auxiliary1 + auxiliary2 + carry_out, 2)
            result = str(auxiliary3) + result
            index1 -= 1
            index2 -= 1
        return result
    
# **********************************************************************************************************
# 69. x 的平方根 
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        l, r, ans = 0, x, x 
        while l <= r:
            mid = l + ((r - l) >> 1)
            if mid * mid > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans

     
# **********************************************************************************************************
# 70. 爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = res[1] =1 
        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[-1]  


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

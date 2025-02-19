class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []  
        cur_length = 0  
        
        for i in range(len(s)):
            #dvdf
            if s[i] in arr:
                #this is the duplicate character -> this will find the first occurence of that character
                arr = arr[arr.index(s[i]) + 1:]
            arr.append(s[i])  
            print(arr)
            cur_length = max(cur_length, len(arr)) 
        
        return cur_length
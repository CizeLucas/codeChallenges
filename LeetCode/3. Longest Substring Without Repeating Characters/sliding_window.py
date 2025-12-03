class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        left = 0
        right = 0
        char_set = set()
        
        for right in range(len(s)): # Sliding Window Concept
            while(s[right] in char_set):
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result

    print(lengthOfLongestSubstring(sum, "pwwkew"))

# pwwkew -> 

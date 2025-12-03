class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0

        for i in range(len(s)):
            string = s[i:]
            stringSet = set()
            substring = ""

            for char in string:                
                if(char in stringSet):
                    print("Contains: " + char)
                    print("MaxLength: " + str(maxLength))
                    print("Substring: " + substring)
                    break

                stringSet.add(char)
                substring += char
                maxLength = max(maxLength, len(substring))
    
        return maxLength

    print(lengthOfLongestSubstring(sum, " "))

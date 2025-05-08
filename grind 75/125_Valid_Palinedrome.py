class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process input string, clean it by removing non-alphanumerics chars
        # upper to lower first? or regex for both
        # O(2n) -> O(n)
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # empty string is true case
        if cleaned == '':
            return True
    
        # one loop, half of length of n
        # get start and end of string
        start, end = 0, len(cleaned) - 1
        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start += 1
            end += -1
        
        return True
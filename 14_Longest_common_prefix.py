class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        elif len(strs) ==1:
            return strs[0]
        
        first = strs[0]
        flen = len(first)
        for s in strs[1:]:
            while first!=s[0:flen]:
                first = first[0:(flen-1)]
                flen -=1
                
                if flen ==0:
                    return ""
        print(first)
            

a = Solution()
strs = ["flower","flow","flight"]

Solution.longestCommonPrefix(a, strs)
# method 1

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict=set(wordDict)
        def helper(word):
            if(len(word)==0):
                return(True)
            for i in range(len(word)+1,0,-1):
                if(word[0:i] in wordDict):
                    if(helper(word[i:])==True):
                        return(True)
            return(False)
        ans=helper(s)
        return(ans)

# method 2
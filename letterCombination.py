class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(len(digits)==0):
            return([])
        ret=[]
        hmap={}
        hmap["2"]=["a","b","c"]
        hmap["3"]=["d","e","f"]
        hmap["4"]=["g","h","i"]
        hmap["5"]=["j","k","l"]
        hmap["6"]=["m","n","o"]
        hmap["7"]=["p","q","r","s"]
        hmap["8"]=["t","u","v"]
        hmap["9"]=["w","x","y","z"]
        n=len(digits)
        def helper(digits,path=""):
            if(len(digits)==0):
                ret.append(path)
                return("")
            for i in hmap[digits[0]]:
                helper(digits[1:],path+i)
        helper(digits)
        return(ret)
o=Solution()
aa=o.letterCombinations("")
print(aa)
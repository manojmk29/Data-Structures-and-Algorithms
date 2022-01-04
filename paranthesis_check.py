class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr=[]
        for i in s:
            if(len(arr)==0):
                arr.append(i)
            else:
                if(arr[-1]=="("):
                    if(i==")"):
                        arr.pop()
                    else:
                        arr.append(i)
                elif(arr[-1]=="["):
                    if(i=="]"):
                        arr.pop()
                    else:
                        arr.append(i)
                elif(arr[-1]=="{"):
                    if(i=="}"):
                        arr.pop()
                    else:
                        arr.append(i)
        if(len(arr)==0):
            return(True)
        else:
            return(False)
s=Solution()
print(s.isValid("()[]{}"))
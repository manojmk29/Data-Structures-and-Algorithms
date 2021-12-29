from typing import DefaultDict
from collections import defaultdict
import sys
sys.setrecursionlimit(15000)
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        ret=[]
        hname={}
        for i in range(len(recipes)):
            hname[recipes[i]]=i
        hmap=defaultdict(lambda :False)
        def helper(i):
            if(hmap[i]==True):
                return(True)
            rc=recipes[i]
            for ing in ingredients[i]:
                if(ing not in supplies):
                    if(ing not in recipes):
                        return(False)
                    elif(helper(hname[ing])==False):
                        return(False)
            ret.append(rc)
            hmap[i]=True
            return(True)
        for i in range(len(recipes)):
            if(hmap[i]==False):
                helper(i)
        return(ret)
obj=Solution()
print(obj.findAllRecipes(["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"],[["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]],["wi","otr","wbjr","fzr","xgp"]))

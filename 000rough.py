word="aab"
arr=[]
k=1
def backtrack(word,temp):
    if(len(word)==0):
        arr.append(temp[:])
        return
    for i in range(0,len(word)):
        now=word[0:i+1]
        if(now==now[::-1]):
            backtrack(word[i+1:],temp+[now])
backtrack(word,[])
print(arr)
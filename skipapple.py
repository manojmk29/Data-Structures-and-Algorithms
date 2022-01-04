def skipapple(word):
    if(len(word)==0):
        return("")
    if((len(word)>=5) and (word[0:5]=="apple")):
        return(skipapple(word[5:]))
    else:
        return(word[0]+skipapple(word[1:]))
print(skipapple("manojlikesappleandorange"))
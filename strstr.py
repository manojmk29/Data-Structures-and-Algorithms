#brute_force
# def strstr_brute(text,match):
#     tl=len(text)
#     ml=len(match)
#     for i in range(0,tl-ml+1):
#         count=0
#         temp=i
#         for j in range(ml):
#             if(text[i]!=match[j]):
#                 break
#             else:
#                 i+=1
#                 count+=1
#         if(count==ml):
#             print("match is found at ",temp,"th position")
#             return
#     print("not found")
#     return
# strstr_brute("abcdd","cdd")
def strstr_rabin(text,match):
    tl=len(text)
    ml=len(match)
    if(tl<ml):
        print("none sorry")
        return
    if(tl==ml):
        if(text==match):
            print("it is present in 0th index")
            return
        else:
            print("none sorry")
        return
    mul=256
    pri=1000000007
    ph=0
    th=0
    rem=1
    for _ in range(ml-1):
        rem*=mul
        rem%=pri
    for i in range(ml):
        ph+=((ph*mul)+ord(match[i]))%pri
        th+=((ph*mul)+ord(text[i]))%pri
    for i in range(tl-ml+1):
        if(ph==th):
            if(text[i:i+ml]==match):
                print("found at ",i,"th pos")
                return
        elif(i!=tl-ml):
            th=(th-(rem*ord(text[i])))%pri
            th*=mul
            th=(th+(ord(text[i+ml])))%pri
        if(tl<0):
            tl+=pri
    print("not found")
    return
# strstr_rabin("abcdd","cdd")
#  if(tl<ml):
#         print("none sorry")
#         return
#     if(tl==ml):
#         if(text==match):
#             print("it is present in 0th index")
#             return
#         else:
#             print("none sorry")
#         return
def strstr_rabin_no(text,match):
    txt_len=len(text)
    pat_len=len(match)
    mul=256
    pat_hash=0
    txt_hash=0
    del_value=1
    for _ in range(pat_len-1):
        del_value*=mul
    for i in range(pat_len):
        pat_hash=((pat_hash*mul)+ord(match[i]))
        txt_hash=((txt_hash*mul)+ord(text[i]))
    for i in range(txt_len-pat_len+1):
        if(pat_hash==txt_hash):
            # print("found at ",i,"th pos")
            if(text[i:i+pat_len]==match):
                print("found at ",i,"th pos")
                return
        if(i!=txt_len-pat_len):
            txt_hash-=(del_value*ord(text[i]))
            txt_hash*=mul
            txt_hash+=ord(text[i+pat_len])
    print("not found")
    return
if(__name__=="__main__"):
    strstr_rabin_no("abcdd","cdd")
    # a="abcdd"
    # b="cdd"
    # print(a[2:5]==b)
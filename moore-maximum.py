def moores_majaority(nums):
    count=0
    element=-1
    for i in nums:
        if(count==0):
            element=i
        if(i==element):
            count+=1
        else:
            count-=1
    return(element)
    
def moores_majaority(nums):
    count1=0
    element1=-1
    count2=0
    element2=-1
    for i in nums:
        if(count1==0):
            element1=i
        if(i==element1):
            count1+=1
        else:
            count1-=1
    return(element1)



nums=[1,1,1,1,2,2,2,2,3,4]
print(moores_majaority(nums))
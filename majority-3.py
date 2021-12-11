def majorityElement(nums,n):
    sz = n;
    num1 = -1
    num2 = -1
    count1 = 0
    count2 = 0
    for i in range(sz):
        if (nums[i] == num1):
            count1+=1
        elif (nums[i] == num2):
            count2+=1
        elif (count1 == 0):
            num1 = nums[i];
            count1 = 1;
        elif (count2 == 0):
            num2 = nums[i];
            count2 = 1;
        else:
            count1-=1
            count2-=1
    ans=[]
    count1 = count2 = 0;
    for i in range(sz):
        if (nums[i] == num1):
            count1+=1
        elif (nums[i] == num2):
            count2+=1
    if (count1 > sz / 3):
        ans.append(num1);
    if (count2 > sz / 3):
        ans.append(num2);
    return ans
arr=[1,2,3,1,1,4,5,5,1,5,6]
print(majorityElement(arr,len(arr)))
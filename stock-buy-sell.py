def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #method 1 o(n^2) time limit exceeded
        
        # max_sum=0
        # for i in range(0,len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         max_sum=max(max_sum,(prices[j]-prices[i]))
        # return max_sum
        
        #method 2 o(n)
        
        min_value=prices[0]
        max_value=0
        for i in range(1,len(prices)):
            max_value=max(max_value,(prices[i]-min_value))
            min_value=min(min_value,prices[i])
        return max_value

         #method 3
         
        l=0
        r=1
        max_val=0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                max_val=max(max_val,(prices[r]-prices[l]))
            else:
                l=r
            r+=1
        return max_val
            
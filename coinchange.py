#recursion 
def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ret=[float("inf")]
        def helper(tot=0,coin_len=0,tot_coin=0):
            if(tot>amount or coin_len==len(coins)):
                return
            if(tot==amount):
                ret[0]=min(ret[0],tot_coin)
                return
            helper(tot+coins[coin_len],coin_len,tot_coin+1)
            helper(tot,coin_len+1,tot_coin)
        helper(0,0,0)
        # for i in range(len(coins)):
        #     helper(0,i,0)
        if(ret[0]==float("inf")):
            return(-1)
        else:
            return(ret[0])
            
def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ret=[float("inf")]
        hmap={}
        hmap[0]=0
        def helper(tot=amount,tot_coin=0):
            if(tot in hmap):
                return(hmap[tot])
            if(tot<0):
                return(float("inf"))
            if(tot==0):
                ret[0]=min(ret[0],tot_coin)
                return(tot_coin)
            hmap[tot]=float("inf")
            for i in range(len(coins)):
                hmap[tot]=min(hmap[tot],helper(tot-coins[i],tot_coin+1))
        helper(amount,0)
        if(ret[0]==float("inf")):
            return(-1)
        else:
            return(ret[0])
print(coinChange([8,2,4],3))
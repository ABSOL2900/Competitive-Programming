/**
 * @param {number[]} piles
 * @return {number}
 */
 var maxCoins = function(piles) {
    
    piles.sort((a,b)=>{
        if(a>b)
            {
                return -1
            }
        else if(a<b)
            {
                return 1
            }
        else return 0
    })
        
        let ans=0
        let left=0
        let right=piles.length-1
        
        while(left<right)
            {
                
                ans+=piles[left+1]
                right-=1
                left+=2
                
            }
    
        return ans
};
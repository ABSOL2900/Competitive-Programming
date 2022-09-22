/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var maxFrequency = function(nums, k) {
    
    let left=0
    let right=0
    let total=0
    let output=0
    
      nums.sort((a,b)=>{
         if(a<b)
             {
                 return -1
             }
         else if(a>b)
             {
                 return 1
             }
         else
             {
                 return 0
             }
     })
 
    
   while(right<nums.length)
       {
           total+=nums[right]
          
           
           while(nums[right]*(right-left+1)>total+k)
               {
                    total-=nums[left]
               left+=1
                   
               }
           
            output= Math.max(output,right-left+1)
           right+=1
       }
     
     return output
 };
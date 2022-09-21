/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var targetIndices = function(nums, target) {
   
  
    for(let i=0;i<nums.length;i++)
        {
            
            for(let j=i;j<nums.length;j++)
                {
                    if(nums[i]!==nums[j])
                        {
                            if(nums[i]>nums[j])
                                {
                                      let temp=nums[j]
                                      nums[j]=nums[i]
                                      nums[i]=temp
                                }
                        }
                }
        }
    let index=[]
    
     for(let i=0;i<nums.length;i++)
         {
             if(nums[i]==target)
                 {
                     index.push(i)
                 }
         }
    
    return index
};
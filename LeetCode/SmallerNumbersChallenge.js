/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var smallerNumbersThanCurrent = function(nums) {
    
     
    let outputarr=[]
    
    for(let i=0;i<nums.length;i++)
        {
            let sum=0
            for(let j=0;j<nums.length;j++)
                {
                    
                    if(nums[i]!==nums[j])
                    {
                    if(nums[i]>nums[j])
                        {
                            sum+=1
                        }
                    }
                }
            outputarr.push(sum)
        }

    
    return outputarr
};
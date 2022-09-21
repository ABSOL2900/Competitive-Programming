/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var sortColors = function(nums) {
    
    let colorarr=[]
    for(let i=0;i<3;i++)
        {
            for(let j=0;j<nums.length;j++)
                {
                    if(nums[j]==i)
                        {
                            colorarr.push(nums[j])
                        }
                }
        }
    
    for(let i=0;i<nums.length;i++)
        {
            nums[i]=colorarr[i]
        }
    
};
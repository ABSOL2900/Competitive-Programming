/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var maxOperations = function(nums, k) {
    
    nums.sort((a,b)=>{
        if(a>b)
            {
                return 1
            }
        else if(a<b)
            {
                return -1
            }
        else return 0
    })
   

    let left=0
    let right=nums.length-1
    let ans=0



    while(left<right)
    {
        if(nums[left]+nums[right]==k)
        {
            ans++
            right--
            left++
        }
        else if(nums[left]+nums[right]<k)
        {
            left++
        }
        else 
        {
            right--
        }
    }

    return ans
};

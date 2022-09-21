/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    
  
    let freqpair=[]
    for(let i=0;i<nums.length;i++)
        {
              let sum=0
            let obj={index:i,value:nums[i]}
            for(let j=i;j<nums.length;j++)
                {
                  
                    if(nums[i]==nums[j])
                        {
                            sum+=1
                        }

                }
                    if(findifExist(nums[i],freqpair)==false)
                       {
                             obj.freq=sum
                           freqpair.push(obj)
                       }
                      
        }
    
    freqpair.sort((a,b)=>{
        if(a.freq<b.freq)
            {
                return 1
            }
        else if(a.freq>b.freq)
            {
                return -1
            }
        else return 0
    })
    
    let output=[]

    for(let i=0;i<k;i++)
        {
            output.push(freqpair[i].value)
        }
    
    return output
   
};

function findifExist(num,arr)
{
    let found=false
    arr.forEach((pair)=>{
        if(pair.value==num)
            {
                found=true
            }
    })
    
return found
}
/**
 * @param {number[]} nums
 * @return {number}
 */
 var numIdenticalPairs = function(nums) {
    
    let pairarr=[]
     
     for(let i=0;i<nums.length;i++)
         {
             for(let j=i+1;j<nums.length;j++)
                 {
                     console.log(i,j)
                     if(nums[i]==nums[j] )
                         {
                             if(pairarr.length==0)
                                 {
                             pairarr.push({i,j})
                                 }else
                                     {
                                         let found=false
                                         pairarr.forEach(pair=>{
                                             if(pair.i==i && pair.j==j)
                                                 {
                                                    found=true
                                                 }
                                         })
                                         if(found==false)
                                         {
                                             pairarr.push({i,j})
                                         }
                                     }
                         }
                 }
         }
     return pairarr.length
     
 };
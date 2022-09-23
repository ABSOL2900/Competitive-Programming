/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var rearrangeArray = function(nums) {
    
    nums.sort((a,b)=>{
       if(a>b){
           return 1
       }
       else if(a<b)
           {
               return -1
           }
       else
           {
               return 0
           }
   })
   
   let median=Math.ceil(nums.length/2)

   
   
   let left=0
   let right=median
   let newarr=[]
   
   
   while(newarr.length!=nums.length)
       {
          
           for(let i=newarr.length-1;i<newarr.length;i++)
               {
                   if(i%2==0)
                       {
                          
                            newarr.push(nums[right])
                           right+=1
                           break
                       }
                   else
                       {
                           newarr.push(nums[left])
                           left+=1
                           break
                       }
               }
       }
   
   return newarr
   
};
/**
 * @param {number[]} nums
 * @return {string}
 */
 var largestNumber = function(nums) {
    
    
    var res = nums.sort(function (a, b) {
         let data=0
       var str1 = '' + a + b;
       var str2 = '' + b + a;
      if( str1 > str2 )
          {
              data=-1
          }
         else
             {
                 data=1
             }
       return data
     })
 
     output=""
     res.forEach(number => {
         output+=number.toString()
     });
   
   return output[0]=='0' ? '0' : output
 };
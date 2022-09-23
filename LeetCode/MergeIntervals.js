/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    
    for(let i=0;i<intervals.length-1;i++)
      {
         for(let j=i+1;j<intervals.length;j++)
         {
             if(intervals[i][0]>intervals[j][0])
             {
                 let temp=intervals[i]
                  intervals[i]=intervals[j]
                 intervals[j]=temp
             }
         }
      }
 
 
      let output=[]
      output.push(intervals[0])
      for(let i=1;i<intervals.length;i++)
      {
         
         if(intervals[i][0]<=output[output.length-1][1])
         {
             let biggest=intervals[i][1]>output[output.length-1][1] ? intervals[i][1] : output[output.length-1][1]
             output[output.length-1][1]=biggest
             
         }
         else output.push(intervals[i])
      }
 
 return output 
     
 };
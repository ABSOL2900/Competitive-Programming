/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    
    let stack=[]
  
  let first =['(','{','[']
  let last=[')','}',']']
  let all=[['{','}'],['(',')'],['[',']']]
  
  
  for(let i=0;i<s.length;i++)
      {
          if(stack.length==0)
              {
                  stack.push(s.charAt(i))
              }
          else{
              if(first.includes(s.charAt(i)))
                  {
                      stack.push(s.charAt(i))
                  }
              else if(last.includes(s.charAt(i)))
                 {
                     if(first.includes(stack[stack.length-1]))
                         {
                             let pop=false
                             all.forEach(arr=>{
                                 if(arr[1]==s.charAt(i) && arr[0]==stack[stack.length-1])
                                     {
                                        pop=true
                                     }
                             })
                             if(pop==true)
                                 {
                                     stack.pop()
                                 }
                             else stack.push(s.charAt(i))
                         }
                     else{
                         stack.push()
                     }
                 }
          }
           

      }

     
  
  return stack.length==0 ? true : false
};
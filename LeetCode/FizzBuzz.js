/**
 * @param {number} n
 * @return {string[]}
 */
 var fizzBuzz = function(n) {
    
    let stringarr=[]
    
    for(let i=1;i<=n;i++)
        {
            let three=false
            let five=false
            if(i%3==0)
                {
                    three=true
                    
                }
            if(i%5==0)
                {
                    five=true
                   
                }
             if(three==true && five==true)
                {
                    stringarr.push("FizzBuzz")
                    
                }
            else if(three==true && five==false)
                {
                    stringarr.push("Fizz")
                    
                    
                }
            else if(three==false && five==true)
                {
                    stringarr.push("Buzz")
                    
                    
                }
            else 
                {
                    stringarr.push(i.toString())
                }
        }
    
    return stringarr
    
};
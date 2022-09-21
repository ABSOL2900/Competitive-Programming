/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    
     
    let stringarr=s.split(" ")
    let updatedarr=[]
    for(let i=0;i<stringarr.length;i++)
    {
        updatedarr.push("")
    }
    stringarr.forEach(str=>{
        let index=str.charAt(str.length-1)
        updatedarr[index]=str.slice(0,str.length-1)
    })

    let sentence=""
    updatedarr.forEach(word=>{
        sentence+=word + " "
    })
    return sentence.trim()
    
};
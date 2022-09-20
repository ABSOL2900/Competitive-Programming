function gradingStudents(grades) {
    // Write your code here
    let gradearr=[]
    grades.forEach(grade=>{
        let nxtmultipleoffive=Math.ceil(grade/5)*5
        
        let gradetopush=0
        if(nxtmultipleoffive-grade<3 && nxtmultipleoffive>=40)
        {
            
            gradetopush=nxtmultipleoffive
        }
        else 
        {
            gradetopush=grade
        }
        gradearr.push(gradetopush)
    })
    
    return gradearr
}


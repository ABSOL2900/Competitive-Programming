function insertionSort1(n, arr) {
    // Write your code here

    let indexoflastnum=arr.length-1
   
   loop2: for(let i=arr.length-1;i>=0;i--)
    {
       
       let printarr=[]
       if(arr[i-1]>arr[i])
       {
      console.log(arr[i-1])
        let temp=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=temp
        indexoflastnum-=1
      loop1: 
       for(let j=0;j<arr.length;j++)
       {
        if(arr[j]==arr[indexoflastnum])
        {
            printarr.push(arr[j+1])
        }
        else
        {
            printarr.push(arr[j])
        }
       }
       console.log(...printarr)

    }else
    {
        console.log(...arr)
        break loop2
    }

       
    }
}




insertionSort1(5,[2,4,6,8,9,3])
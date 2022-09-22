
var MinStack = function() {
    this.stack1=[]
    this.minindex=0;
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    
    if(this.stack1.length==0)
        {
            this.minindex=0
           
        }
    else if(val<this.stack1[this.minindex])
        {
            this.minindex=this.stack1.length
        }
    this.stack1.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  
    this.stack1.pop()
      if(this.stack1.length==0)
        {
            this.minindex=0
           
        }else{
     this.minindex=this.stack1.indexOf(Math.min(...this.stack1))
        }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack1[this.stack1.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack1[this.minindex]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_fruit=-1
        second_last_fruit=-1
        curr_max=0
        last_fruit_count=0
        res=0
        for fruit in fruits:
            if fruit==last_fruit or fruit==second_last_fruit:
                curr_max+=1
            else:
                curr_max=last_fruit_count+1
                
            if fruit==last_fruit:
                last_fruit_count+=1
            else:
                last_fruit_count=1
            res=max(curr_max,res)
            if fruit!=last_fruit:
                second_last_fruit, last_fruit=last_fruit, fruit
        return res
                
        
if len(nums)==1:
            return nums
        sorted_arr=sorted(nums,reverse=True)
        s=sum(sorted_arr)
        great_sum=sorted_arr[0] + sorted_arr[1]
        j=2
        count=2
        while (s-great_sum)>=great_sum:
            great_sum+=sorted_arr[j]
            j+=1
            count+=1
        largest=sorted_arr[0]
        sum1=0
        for i in sorted_arr[1:]:
            sum1+=i
        if largest>sum1:
            return[largest]
        else:
            return(sorted_arr[:count])
        
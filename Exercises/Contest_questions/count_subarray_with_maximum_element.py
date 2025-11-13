def countMajoritySubarrays(nums, target):
        transformed_arr=[]
        for num in nums:
            if num == target:
                transformed_arr.append(1)
            else:
                transformed_arr.append(-1)
        count = 0
        prefix_sum = 0
        prefix_arr = [0]
        for value in transformed_arr:
            prefix_sum = value + prefix_arr[-1] # last item
            prefix_arr.append(prefix_sum)

        print(transformed_arr,prefix_arr)
        for i in range(len(prefix_arr)-1):
                for j in range(i,len(prefix_arr)-1):
                    print(i,j)
                    if prefix_arr[j+1]-prefix_arr[i]>0:
                        count+=1
        print(count)
        return count

# countMajoritySubarrays([1,2,2,3],2)
countMajoritySubarrays([1,1,1,1],1)
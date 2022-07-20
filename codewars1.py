def find_uniq(arr):
    # your code here
    uniq_arr=set(arr)
    
    for i in uniq_arr:
        i_ctr=0
        for j in arr:         
            if i==j:
                i_ctr+=1
            if i_ctr>1:
                break
        if i_ctr==1:
            return i

    # return n   # n: unique number in the array

result=find_uniq([2, 1, 1, 1, 1, 1])
print(result)

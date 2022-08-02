def func(nums):
    nums_list=[int(x) for x in nums.split()]
    nums_list.pop(0)
    avg=sum(nums_list)/len(nums_list)
    best_result=max(nums_list)

    for num in nums_list:
        if abs(avg - num)<best_result:
            result=num
            best_result=abs(avg - num)
        if best_result==0:
            print(num)
            return None
    
    print(result)

for _ in range(int(input())):
    func(input())
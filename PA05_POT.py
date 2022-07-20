def pot(str):
    list=str.split()
    temp_ctr=0
    temp_int=0

    while temp_ctr<int(input_d):
        res=int(list[temp_int])**int(list[temp_int+1])
        res_str=repr(res)
        result=res_str[-1]

        temp_ctr+=1
        temp_int+=2
        print(result)

    return int(result)

input_d=input()
pot(input())

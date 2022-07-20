input_list=[]

it_num=int(input())

for _ in list(range(0, it_num)):
    input_list.append(input())

for x in input_list:
    temp_list=x.split()
    v1=int(temp_list[0])
    v2=int(temp_list[1])
    print(int((2*v1*v2)/(v1+v2)))

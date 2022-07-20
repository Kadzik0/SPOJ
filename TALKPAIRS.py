height_list=[]

number_of_ppl=int(input())

height_string=input()

height_list=height_string.split()

result=number_of_ppl-1

for index_i, value_i in enumerate(height_list):
    for index_j, value_j in enumerate(height_list):
        if index_i<index_j:
            if height_list[index_j]>height_list[index_j-1]:
                result+=1
            else:
                break


print(result)
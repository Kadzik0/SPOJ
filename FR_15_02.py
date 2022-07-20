list_input=[]
tuple_size=int(input())

while tuple_size!=0:
    temp_string=""
    input_string=input()
    for index, value in enumerate(input_string):
        
        if value==' ':
            temp_string=input_string[:index]
    list_input.append(int(temp_string))

    tuple_size-=1

print(len(set(list_input)))
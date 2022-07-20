str_input=input()
list_input=[]
for i in str_input.split():
    list_input.append(int(i))


print(list_input[0]*list_input[1]+list_input[2]*list_input[3])

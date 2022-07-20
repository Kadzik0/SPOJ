def pp0504b(char):
    list_char=char.split()
    result=''

    if len(list_char[0])>=len(list_char[1]):
        iteration_num=len(list_char[1])
    else:
        iteration_num=len(list_char[0])

    for x in range(iteration_num):
        result+=list_char[0][x]+list_char[1][x]

    print(result)


for _ in range(int(input())):
    pp0504b(input())
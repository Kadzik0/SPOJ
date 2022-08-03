while True:
    try:
        input_string=input()

        temp_list=input_string.split()
        num_list=[int(x) for x in temp_list[1::]]

        if temp_list[0]=="+":
            print((num_list[0]+num_list[1]))
            continue

        if temp_list[0]=='-':
            print(num_list[0]-num_list[1])
            continue

        if temp_list[0]=='*':
            print(num_list[0]*num_list[1])
            continue

        if temp_list[0]=='/':
            print(int(num_list[0]/num_list[1]))
            continue

        if temp_list[0]=='%':
            print(num_list[0]%num_list[1])
            continue
    except EOFError:
        break

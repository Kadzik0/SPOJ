def jrowlin(str):

    list=str.split()

    a=float(list[0])
    b=float(list[1])
    c=float(list[2])

    if a==0:
        if b<c:
            print('BR')
        elif b==c:
            print('NWR')
        else:
            pass
    else:
        res=float((c-b)/a)
        print(round(res, 2))


jrowlin(input())


# iterations number
i=int(input())

while i!=0:
    # counter of modulo=0
    sub_number=0
    # input of tested number
    try:
        inpt=int(input())
        if inpt!=1:
            for j in [int for int in range(1, int(inpt**0.5)+1)]:
                if inpt%j==0:
                    sub_number+=1
                if sub_number>1:
                    break
            if sub_number<=1:
                print('TAK')
            else:
                print('NIE')
        else:
            print('NIE')
        i-=1
    except:
        print('Wrong value')
        break

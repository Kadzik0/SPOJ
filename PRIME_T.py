list=[int for int in range(1,10001)]
i=int(input())

while i!=0:
    sub_number=0
    inpt=int(input())
    for j in list[:int(inpt**0.5)]:
        if inpt%j==0:
            sub_number+=1
        if sub_number>1:
            break
    if inpt==1:
        sub_number=3
            
    if sub_number<=1:
        print('TAK')
    else:
        print('NIE')
    i-=1
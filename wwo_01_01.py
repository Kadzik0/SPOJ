list_num=(input()).split()
list_names1=(input()).split()
list_names2=(input()).split()
list_names3=(input()).split()
list_names=[]

list_num=list(map(int, list_num))

list_names=list_names1+list_names2+list_names3
def func():
    wmn_ctr=0

    for name in list_names:
        if name[-1]=='a':
            wmn_ctr+=1

    man_ctr=sum(list_num)-wmn_ctr

    if wmn_ctr>man_ctr:
        print(man_ctr)
    else:
        print(wmn_ctr)


func()
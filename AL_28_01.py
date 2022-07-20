n=int(input())
s=input()
first_time=True
num=0

iterates=int((n-1)/2)

for _ in list([x for x in range(0,iterates+1)]):
    result=""
    temp_str=s[iterates]
    if first_time==True:
        for _ in list([x for x in range(0,iterates,1)]):
            result+="."

        result+=temp_str

        for _ in list([x for x in range(iterates+1, n)]):
            result+="."
        
        first_time=False
    elif iterates==0:
        result=s    
    else:
        for _ in list([x for x in range(0,iterates,1)]):
            result+="."
        
        result+=s[iterates:-iterates]

        for _ in list ([x for x in range(n-iterates, n)]):
            result+='.'
    iterates-=1
    print(result)
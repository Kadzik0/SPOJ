def fr_10_20(a, b, c):
    result_word=""
    triple_list=b.split()

    for letter in c:
        if letter in triple_list:
            result_word+=2*letter
        else:
            result_word+=letter

    return result_word



a=int(input())
b=input()
c=input()

result=fr_10_20(a,b,c)
print(result)
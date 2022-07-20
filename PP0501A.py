# def NWD(a, b):
#     if a>b:
#         for num in range(1,b+1):
#             if a%num==0 and b%num==0:
#                 temp_nwd=num
            
#         print(temp_nwd)
#     elif a<b:
#         for num in range(1,a+1):
#             if a%num==0 and b%num==0:
#                 temp_nwd=num
            
#         print(temp_nwd)
#     else:
#         print(a)


# for _ in range(int(input())):
#     input_str=input()
#     input_list=input_str.split()
#     a=int(input_list[0])
#     b=int(input_list[1])

#     NWD(a, b)

def NWD(a, b):
    if a>b:
        while a%b!=0:
            rest=a%b
            a=b
            b=rest
        return b
    elif a<b:
        while b%a!=0:
            rest=b%a
            b=a
            a=rest
        return a
    elif a==b:
        return a

for _ in range(int(input())):
     input_list=input().split()
     a=int(input_list[0])
     b=int(input_list[1])

     result=NWD(a, b)
     print(result)
def BFN1(input_nr):
    bfn_nr=input_nr
    iteration_ctr=0
    while True:
        test_string=str(bfn_nr)
        if test_string==test_string[::-1]:
            print(bfn_nr, iteration_ctr)
            break
        else:
            bfn_nr+=int(test_string[::-1])
            iteration_ctr+=1




iteration_counter=int(input())

for _ in range(iteration_counter):

    BFN1(int(input()))


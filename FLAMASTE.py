iterates=int(input())

for _ in range(iterates):
    input_string=input()
    x=0
    new_word=''
    old_letter=''
    new_letter=''
    letter_counter=0

    for index_1, value_1 in enumerate(input_string):
        new_letter=value_1

        if new_letter==old_letter:
            pass
        else:           
            for index_2, value_2 in enumerate(input_string[x:]):
                if value_1==value_2:
                    letter_counter+=1
                else:
                    break

            x+=letter_counter

            if letter_counter==1:
                new_word+=value_1
                letter_counter=0
            elif letter_counter==2:
                new_word+=2*value_1
                letter_counter=0
            elif letter_counter>=3:
                new_word+=value_1+str(letter_counter)
                letter_counter=0

        old_letter=value_1

    print(new_word)

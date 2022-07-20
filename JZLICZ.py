from typing import Counter
import string 

input_string=""

for _ in range(int(input())):
    input_string+=input()

result_dict=Counter(input_string)

for letter in string.ascii_lowercase:
    if letter in result_dict:
        print(f'{letter} {result_dict[letter]}')

for letter in string.ascii_uppercase:
    if letter in result_dict:
        print(f'{letter} {result_dict[letter]}')
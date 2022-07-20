current_sum = 0
while True:
    try:
        current_sum += int(input())
        print(current_sum)
    except EOFError:
        break
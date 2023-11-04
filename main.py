if __name__ == '__main__':
    while True:
        n, rm = map(int, input().split())

        if (n, rm) == (0, 0):
            break

        number = int(input())

        for i in range(n - 1, 1, -1):
            if rm == 0:
                break

            prev_e = 10 ** (i - 1)
            curr_e = prev_e * 10
            prev = number // curr_e
            curr = number // prev_e - prev * 10

            number -= (prev * curr_e)

            if prev > curr:
                number -= (curr * prev_e)
                number += (prev * prev_e)

            rm -= 1

        print(number)

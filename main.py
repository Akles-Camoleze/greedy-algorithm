if __name__ == '__main__':
    while True:
        n, d = map(int, input().split())
        if (n, d) == (0, 0):
            break

        if d < 1 or d >= n or n > 10 ** 5:
            raise RuntimeError("Invalid entry, please verify: (1 ≤ D < N ≤ 10^5)")

        number = int(input())
        for i in range(n - 1, 1, -1):
            if d == 0:
                break

            prev_e = 10 ** (i - 1)
            curr_e = prev_e * 10
            prev = number // curr_e
            curr = number // prev_e - prev * 10

            number -= (prev * curr_e)

            if prev > curr:
                number -= (curr * prev_e)
                number += (prev * prev_e)

            d -= 1

        print(number)

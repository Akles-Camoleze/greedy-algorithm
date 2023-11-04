if __name__ == '__main__':
    while True:
        n, d = map(int, input().split())
        if (n, d) == (0, 0):
            break

        if d < 1 or d >= n or n > 10 ** 5:
            print("Invalid entry, please verify: (1 ≤ D < N ≤ 10^5)")
            continue

        number = input().strip()

        if len(number) != n:
            print(f"Invalid entry, please verify number length is {n}")
            continue

        stack = []
        for digit in number:
            while d > 0 and stack and stack[-1] < digit:
                stack.pop()
                d -= 1
            stack.append(digit)

        while d > 0:
            stack.pop()
            d -= 1

        print(''.join(stack))

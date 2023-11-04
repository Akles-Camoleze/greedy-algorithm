if __name__ == '__main__':
    while True:
        n, d = map(int, input().split())
        if (n, d) == (0, 0):
            break

        if d < 1 or d >= n or n > 10 ** 5:
            raise RuntimeError("Invalid entry, please verify: (1 ≤ D < N ≤ 10^5)")

        number = input().strip()

        if len(number) != n:
            raise RuntimeError(f"Invalid entry, please verify number length is equals: {n}")

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

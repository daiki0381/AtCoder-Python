# https://atcoder.jp/contests/abc207/tasks/abc207_b

def main():
    def solve():
        count = 10**7 + 5
        for x in range(count):
            light_blue = A + B * x
            red = C * x
            if light_blue <= red * D:
                return x
        return -1

    A, B, C, D = map(int, input().split())
    print(solve())

if __name__ == "__main__":
    main()

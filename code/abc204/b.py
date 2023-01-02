# https://atcoder.jp/contests/abc204/tasks/abc204_b

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for a in A:
        if a <= 10:
            continue
        else:
            x = a - 10
            ans += x

    print(ans)

if __name__ == "__main__":
    main()

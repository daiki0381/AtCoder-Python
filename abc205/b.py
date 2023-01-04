# https://atcoder.jp/contests/abc205/tasks/abc205_b

def main():
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(1, N + 1):
        if A.count(i) != 1:
            print("No")
            break
    else:
        print("Yes")

if __name__ == "__main__":
    main()

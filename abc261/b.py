# https://atcoder.jp/contests/abc261/tasks/abc261_b

N = int(input())
A = [input() for _ in range(N)]
is_incorrect = False

for a_index, a in enumerate(A):
    for n in range(N):
        if a_index == n:
            continue
        else:
            if a[n] == "W":
                if A[n][a_index] != "L":
                    is_incorrect = True
                    break
            elif a[n] == "L":
                if A[n][a_index] != "W":
                    is_incorrect = True
                    break
            else:
                if A[n][a_index] != "D":
                    is_incorrect = True
                    break
                
if is_incorrect:
    print("incorrect")
else:
    print("correct")

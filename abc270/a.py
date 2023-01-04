# https://atcoder.jp/contests/abc270/tasks/abc270_a

A, B = map(int, input().split())

def build_solved_problems(total):
    if total == 0:
        return []
    elif total == 1:
        return [1]
    elif total == 2:
        return [2]
    elif total == 4:
        return [4]
    elif total == 3:
        return [1, 2]
    elif total == 5:
        return [1, 4]
    elif total == 6:
        return [2, 4]
    elif total == 7:
        return [1, 2, 4]

takahashi_solved_problems = build_solved_problems(A)
aoki_solved_problems = build_solved_problems(B)
sunuke_solved_problems = {*takahashi_solved_problems, *aoki_solved_problems}
print(sum(sunuke_solved_problems))

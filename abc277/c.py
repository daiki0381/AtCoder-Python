# https://atcoder.jp/contests/abc277/tasks/abc277_c

# 頂点1から探索を始めたときに訪問可能な頂点のうち、最も大きな頂点は何か？

from collections import deque, defaultdict

N = int(input())
d = defaultdict(list)

# ①ある頂点から行ける頂点を格納したリストを生成
for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

# ②キューを用意
que = deque()
que.append(1)

# ③訪問チェックを用意
seen = set()
seen.add(1)

# ④ 訪問後にque,seenに格納
while que:
    now = que.popleft()

    for i in d[now]:
        if i not in seen:
            que.append(i)
            seen.add(i)

print(max(seen))

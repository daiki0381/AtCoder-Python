# https://atcoder.jp/contests/abc284/tasks/abc284_c

from collections import deque, defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
ans = 0

# ①ある頂点から行ける頂点を格納したリストを生成
for _ in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

# ②キューを用意
que = deque()

# ③訪問チェックを用意
seen = set()

# ④同じ連結成分に含まれる頂点を全て「探索済み」にする
for i in range(1, N + 1):
    if i not in seen:
        ans += 1
        que.append(i)
        while que:
            now = que.popleft()
            for i in d[now]:
                if i not in seen:
                    que.append(i)
                    seen.add(i)

print(ans)

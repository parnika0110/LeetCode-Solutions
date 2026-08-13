from typing import List

class Node:
    def __init__(self, l=0, r=0, p=0, s=0, b=0, lc='', rc=''):
        self.l = l
        self.r = r
        self.p = p
        self.s = s
        self.b = b
        self.lc = lc
        self.rc = rc


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        st = [Node() for _ in range(4 * n)]

        def pull(i):
            L = st[i * 2]
            R = st[i * 2 + 1]

            st[i].l = L.l + R.l
            st[i].lc = L.lc
            st[i].rc = R.rc

            st[i].p = L.p
            st[i].s = R.s

            st[i].b = max(L.b, R.b)

            if L.rc == R.lc:
                st[i].b = max(st[i].b, L.s + R.p)

                if L.p == L.l:
                    st[i].p = L.l + R.p

                if R.s == R.l:
                    st[i].s = R.l + L.s

        def build(i, l, r):
            if l == r:
                st[i] = Node(
                    1, 0, 1, 1, 1,
                    s[l], s[l]
                )
                return

            m = (l + r) // 2

            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)

            pull(i)

        def update(i, l, r, pos, ch):
            if l == r:
                st[i].lc = ch
                st[i].rc = ch
                return

            m = (l + r) // 2

            if pos <= m:
                update(i * 2, l, m, pos, ch)
            else:
                update(i * 2 + 1, m + 1, r, pos, ch)

            pull(i)

        build(1, 0, n - 1)

        ans = []

        for ch, pos in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, pos, ch)
            ans.append(st[1].b)

        return ans